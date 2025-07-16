@Clockify @Client_feature
@allure.label.owner:Steven_Ospina
@allure.label.epic:BDD
@allure.label.feature:Clients
Feature:  Suite for clients endpoint from Clockify API

  @allure.label.story:Get_clients
  @acceptance @client_id @clean
  Scenario: Scenario to get all clients
    When user calls "GET" method to "get" "clients" endpoint
    Then the status code is 200

  @allure.label.story:Create_clients
  @Clients @acceptance @clean
  Scenario: Scenario to create client
    When user calls "POST" method to "create" "clients" endpoint using json
    """
    {
      "address": "new address",
      "email": "automation@courseapi.com",
      "name": "steven ospina",
      "note": "client test"
    }
    """
    Then the status code is 201