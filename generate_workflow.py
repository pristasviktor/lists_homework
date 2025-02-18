import json

# Load exercise data from JSON file
with open("exercises.json", "r") as file:
    exercises = json.load(file)

# Start YAML content
yaml_content = """name: Autograding Tests
on:
  - push
  - workflow_dispatch

permissions:
  actions: read
  contents: read

jobs:
  autograding:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install pytest pytest-json-report
"""

# Generate test steps for each exercise
for exercise in exercises:
    exercise_name = exercise["name"].replace(" ", "_")
    
    # Check if 'test_file' exists, otherwise use the default filename
    test_file = exercise.get("test_file", f"tests/{exercise_name.lower()}.py")
    
    yaml_content += f"""
      - name: Run tests for {exercise["name"]}
        id: {exercise_name}
        run: |
          # Set default result (failure)
          echo '{{"version":3,"status":"fail","tests":[{{"name":"{exercise["name"]}","status":"fail","test_code":"","task_id":"{exercise_name}","filename":"{test_file}","line_no":4,"duration":1,"score":0}}],"max_score":{exercise["max_score"]}}}' | base64 -w 0 > {exercise_name}_encoded.txt
          echo "{exercise_name.upper()}_RESULT=$(cat {exercise_name}_encoded.txt)" >> $GITHUB_ENV

          # Run pytest
          pytest -q --json-report --json-report-file={exercise_name}.json {test_file}
          TEST_RESULT=$?

          # Overwrite result on success
          if [ $TEST_RESULT -eq 0 ]; then
            echo '{{"version":3,"status":"pass","tests":[{{"name":"{exercise["name"]}","status":"pass","test_code":"","task_id":"{exercise_name}","filename":"{test_file}","line_no":4,"duration":1,"score":{exercise["max_score"]}}}],"max_score":{exercise["max_score"]}}}' | base64 -w 0 > {exercise_name}_encoded.txt
            echo "{exercise_name.upper()}_RESULT=$(cat {exercise_name}_encoded.txt)" >> $GITHUB_ENV
          fi
        continue-on-error: true
"""

# Add the autograding reporter step
yaml_content += f"""
      - name: Autograding Reporter
        uses: classroom-resources/autograding-grading-reporter@v1
        with:
          runners: {",".join([exercise['name'].replace(" ", "_") for exercise in exercises])}
        env:
"""
for exercise in exercises:
    exercise_name = exercise["name"].replace(" ", "_")
    yaml_content += f"          {exercise_name.upper()}_RESULTS: ${{{{ env.{exercise_name.upper()}_RESULT }}}}\n"

# Save the generated YAML to file
with open(".github/workflows/classroom.yml", "w") as file:
    file.write(yaml_content)

print("✅ GitHub Actions workflow generated successfully: .github/workflows/classroom.yml")
