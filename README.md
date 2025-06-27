# Delete Users

1. Replace <Session User API Access Token> with a valid token
2. Run - python3 get_email_member_id_o11y.py
3. Copy the output to member_ids.txt and retain only the member_ids to be deleted
4. Run - python3 delete_member_id_o11y.py

Note - Deletion of users has been intentionally kept as a 2-step process - to be able to manually validate and retain only the required member_ids to be deleted - and to avoid any inadvertent deletion that may be caused by a single-step process.
