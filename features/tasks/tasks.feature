@Clockify @tasks_feature
@allure.label.owner:Steven_Ospina
@allure.label.epic:BDD
@allure.label.feature:Tasks
Feature:  Suite for Tasks endpoint from Clockify API

  @functional @acceptance @project_id @clean
  Scenario: Scenario to create a task
    When user calls "POST" method to "create" "tasks" endpoint using json
    """
    {
      "name": "Automation",
      "status": "DONE"
    }
    """
  Then the status code is 201