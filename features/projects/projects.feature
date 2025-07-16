@Clockify @projects_feature
@allure.label.owner:Steven_Ospina
@allure.label.epic:BDD
@allure.label.feature:Projects
Feature:  Suite for projects endpoint from Clockify API

  @acceptance @project_id @clean
  Scenario: Scenario to get a Project
    When user calls "GET" method to "get" "projects" endpoint
    Then the status code is 200


  @functional @acceptance @Projects @clean
  Scenario: Scenario to create a Project
    When user calls "POST" method to "create" "projects" endpoint using json
    """
    {
      "name": "project name from feature file",
      "billable": true,
      "isPublic": true
    }
    """
  Then the status code is 201

  @normal
  @functional @acceptance @project_id @clean
  Scenario: Scenario to update a Project
    When user calls "PUT" method to "update" "projects" endpoint using json
    """
    {
      "archived": false,
      "name": "New name",
      "billable": true,
      "isPublic": true
    }
    """
    Then the status code is 200

  @acceptance @project_id
  Scenario: Scenario to delete a project
    When user calls "DELETE" method to "delete" "projects" endpoint
    Then the status code is 200

  @functional @negative
  Scenario: Negative scenario to create a Project without name property
    When user calls "POST" method to "create" "projects" endpoint using json
    """
    {
      "isPublic": true
    }
    """
  Then the status code is 400

  @functional @negative
  Scenario: Negative scenario to create a Project with invalid properties
    When user calls "POST" method to "create" "projects" endpoint using json
    """
    {
      "name": "negative scenario",
      "isPublic": "no"
    }
    """
  Then the status code is 400