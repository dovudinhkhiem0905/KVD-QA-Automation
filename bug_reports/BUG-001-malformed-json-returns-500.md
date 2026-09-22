# BUG-001: Malformed JSON returns 500 instead of 400

## Description
The `/api/quote` endpoint returns HTTP 500 when the request body contains malformed JSON.

## Steps to Reproduce
1. Send a POST request to `/api/quote`
2. Set `Content-Type` to `application/json`
3. Send malformed JSON such as `{bad json`

## Expected Result
The API should return HTTP 400 Bad Request.

## Actual Result
The API returns HTTP 500 Internal Server Error.

## Response
{
  "ok": false,
  "error": "Expected property name or '}' in JSON at position 1 (line 1 column 2)"
}

## Severity
Low / Medium

## Automated Test
`tests/test_quote_api.py::test_quote_api_rejects_malformed_json`