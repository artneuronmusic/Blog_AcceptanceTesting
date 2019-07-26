Feature: Test navigation between pages


  Scenario: Homepage can go to Blog

    Given I am on the home page
    When I click on the link "Go to blog"
    Then I am on the blog page


  Scenario: Blog go to Homepage

    Given I am on the blog page
    When I click on the link "Go to home"
    Then I am on homepage


