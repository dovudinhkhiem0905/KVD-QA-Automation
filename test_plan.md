# KVD Insurance Group - QA Test Plan

## Scope

Initial testing focuses on:
- Contact / quote form
- Client-side form validation
- API behavior
- Error handling
- Input handling
- Responsive behavior
- Duplicate submission prevention

## Test Cases

| ID | Test Scenario | Steps | Expected Result | Priority |
|---|---|---|---|---|
| TC-001 | Submit valid required fields | Enter a valid name and email, then click Submit | Form submits successfully and success message appears | High |

| TC-002 | Submit with empty name | Leave name blank, enter a valid email, then click Submit | Browser prevents submission | High |

| TC-003 | Submit with empty email | Enter a name, leave email blank, then click Submit | Browser prevents submission | High |

| TC-004 | Submit invalid email format | Enter an invalid email such as `abc`, then click Submit | Browser prevents submission | High |

| TC-005 | Submit all form fields | Enter valid values for name, email, phone, address, coverage, and message | Form submits successfully and data is processed | High |

| TC-006 | Submit only required fields | Enter only name and email and leave all optional fields empty | Form submits successfully | Medium |

| TC-007 | Submit Vietnamese / Unicode characters | Enter values such as `Nguyễn Văn An` and Vietnamese text, then submit | Characters are preserved correctly and submission succeeds | Medium |

| TC-008 | Submit form multiple times quickly | Click Submit repeatedly before the first request finishes | Only one intended submission should be processed and duplicate leads should be prevented | High |

| TC-009 | Submit HTML-like input | Enter text such as `<b>Hello</b>` or `<script>alert('test')</script>` in the message field | Input is handled safely and is not executed as HTML or script | High |

| TC-010 | Submit request directly to API without required fields | Send a POST request to `/api/quote` without name or email | API should reject invalid input with a controlled error response | High |

| TC-011 | Send malformed JSON to API | Send invalid JSON to `/api/quote` | API returns a controlled error response and does not crash the application | High |

| TC-012 | Handle API/server failure | Cause the quote API to return an error during form submission | User sees an error message and the page remains usable | High |

| TC-013 | Test mobile viewport | Open the contact form on a small mobile screen | Form remains readable, fields stay within the viewport, and Submit remains usable | High |