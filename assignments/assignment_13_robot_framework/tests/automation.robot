*** Settings ***
Library    SeleniumLibrary
Library    RequestsLibrary
Library    libraries.CustomKeywords

Test Setup       Open Browser And Login
Test Teardown    Close All Browsers

*** Variables ***
${URL}            https://www.saucedemo.com/
${BROWSER}        chrome
${USERNAME}       standard_user
${PASSWORD}       secret_sauce
${API_URL}        https://jsonplaceholder.typicode.com
${TODO_ID}        1

*** Test Cases ***
Login And Verify Product Page
    [Tags]    smoke    ui
    Title Should Be    Swag Labs
    Page Should Contain    Products
    Log    Successful login verified

Calculate Sum Using Python Keyword
    [Tags]    python    utility
    ${result}=    Add Numbers    10    25
    Should Be Equal As Integers    ${result}    35
    Log    Sum result: ${result}

Verify Todo API Response
    [Tags]    api
    Create Session    todo_session    ${API_URL}
    ${response}=    GET On Session    todo_session    /todos/${TODO_ID}
    Should Be Equal As Strings    ${response.status_code}    200
    ${data}=    Evaluate    $response.json()
    Should Be Equal As Integers    ${data}[id]    ${TODO_ID}
    Log    API response verified for Todo ID ${TODO_ID}

*** Keywords ***
Open Browser And Login
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Input Text    id=user-name    ${USERNAME}
    Input Password    id=password    ${PASSWORD}
    Click Button    id=login-button
    Wait Until Page Contains    Products    10s
