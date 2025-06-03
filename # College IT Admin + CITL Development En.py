# College IT Admin + CITL Development Environment Scaffold
# Author: FLEX Coding GPT
# Purpose: Initialize standard folders and README.md templates for future automation projects

import os

# Base project structure
BASE_DIR = "CollegeAutomationSuite"

# Stack definitions
admin_stacks = [
    "STACK_SharePointAdmin",
    "STACK_PowerAutomateTools",
    "STACK_GraphAPIManagement",
    "STACK_OutlookExchangeAutomation",
    "STACK_TeamsBotIntegration",
    "STACK_AIIntegrations",
    "STACK_CanvasIntegration",
    "STACK_SharedLibraries",
    "DEV_SandboxTools"
]

citl_stacks = [
    "STACK_SharePointForms",
    "STACK_FlowAutomationTranscripts",
    "STACK_StudentTemplates",
    "STACK_CITL_ReportsAndMacros",
    "CITL_Reference_Guides"
]

def create_stack(path, stack_name):
    stack_path = os.path.join(path, stack_name)
    os.makedirs(os.path.join(stack_path, "src"), exist_ok=True)
    os.makedirs(os.path.join(stack_path, "docs"), exist_ok=True)
    os.makedirs(os.path.join(stack_path, "tests"), exist_ok=True)
    os.makedirs(os.path.join(stack_path, ".vscode"), exist_ok=True)
    with open(os.path.join(stack_path, "README.md"), "w") as f:
        f.write(f"# {stack_name}\n\n" +
                "This is a root stack folder prepared for future development projects.\n\n" +
                "## Structure:\n" +
                "- `src/`: Source code\n" +
                "- `docs/`: Documentation\n" +
                "- `tests/`: Unit and integration tests\n")

# Create base folders
admin_root = os.path.join(BASE_DIR, "AdminProjects")
citl_root = os.path.join(BASE_DIR, "CITL_AutomationProjects")
doc_root = os.path.join(BASE_DIR, "SOLUTION_DOCUMENTATION")

os.makedirs(admin_root, exist_ok=True)
os.makedirs(citl_root, exist_ok=True)
os.makedirs(doc_root, exist_ok=True)

# Create stacks
for stack in admin_stacks:
    create_stack(admin_root, stack)

for stack in citl_stacks:
    create_stack(citl_root, stack)

# Create top-level documentation files
with open(os.path.join(doc_root, "IntegrationMatrix.xlsx"), "w") as f:
    f.write("")  # Placeholder
with open(os.path.join(doc_root, "StackRoles.md"), "w") as f:
    f.write("# Stack Roles\n\nDescribe ownership and responsibilities for each stack.")
with open(os.path.join(doc_root, "DevSetupInstructions.md"), "w") as f:
    f.write("# Dev Setup Instructions\n\nDocument your environment, SDK installs, and dependencies here.")

print(f"Scaffold complete. Navigate to `{BASE_DIR}` to begin development.")
