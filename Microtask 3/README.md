# Microtask #3

Based on the JSON documents produced by Perceval and its source code, try to answer the following questions:

1. What is the meaning of the JSON attribute 'timestamp'?

Timestamp is used to represent the time when the item was fetched by perceval.
```
'timestamp': datetime_utcnow().timestamp()
```
This date is converted to UNIX timestamp format.

***

2. What is the meaning of the JSON attribute 'updated_on'?

“Updated_on” is the date when the last change was made to the item.

“Updated_at” is the date when the item was last updated.

>"updated_on" is the latest date among all "update_at" dates for an item.

The "updated_on" attribute is calculated considering all the "updated_at" attributes of that item.

"updated_at" attribute indicates date for any new change made to the item like comments, reactions, etc.
"updated_at" is defined for every change to the item.

In the case of github, the "updated_on" is obtained from the attribute "updated_at" of issues/pull requests. 

"updated_on" is then calculated for the entire item and it gives the overall idea of when the item was last modified.


***

3. What is the meaning of the JSON attribute 'origin'?

```
"origin": "https://github.com/Sentdex/sentdebot" 
```

Origin attribute gives the URL of the repo.

It is  the same for all the fetched json objects.


***

4. What is the meaning of the JSON attribute 'category'?

Category attribute indicates the type of object fetched for a given backend.


| Backend  | Categories   |
|--------- | ------------ |
| askbot | question |
| bugzilla | bug |
| bugzillarest | bug |
| confluence | historical content |
| discourse | topic |
| dockerhub | dockerhub-data |
| gerrit | review |
| git | commit |
| GitHub   | issue / pull request / repository|
| GitLab   | issue / merge_request |
| googlehits | google_hits |
| groupsio | message |
| hyperkitty | message |
| jenkins | build | 
| jira | issue |
| launchpad | issue |
| mattermost | post |
| mbox | message |
| mediawiki | page |
| meetup | event |
| nntp | article |
| pagure | issue |
| phabricator | task |
| pipermail | message |
| redmine | issue |
| rss | entry |
| slack | message |
| stackexchange | question |
| supybot | message |
| telegram | message |
| twitter | tweet |


***

5. How many categories do the GitHub and GitLab backends have?

GitHub backend has 3 categories - 'issue', 'pull request', 'repository'.

GitLab backend has 'issue' or 'merge_request'.


***

6. What is the meaning of the JSON attribute 'uuid'?

'uuid' is used to uniquely identify a perceval item.

The 'uuid' is the SHA1 of the concatenation of origin of the item and identifier from the GitHub/GitLab  item (item_id).


***

7. What is the meaning of the JSON attribute search_fields?

Search_fields is useful to inspect a Perceval item without entering in the attribute data.

It shows the attributes useful to perform queries/searches.

GitHub : search_field contains item_id,owner and repo.

GitLab : search_field contains 
* item_id, 
* owner
* iid
 >id is unique across all issues and is used for any API call, whereas iid is unique only in scope of a single project. When you browse issues or merge requests with the Web UI, you see the iid.
* Project
* groups
 >if the project is part of a (nested) group, all groups are also included to the search fields via the attribute 'groups'.

***

8. What is stored in the attribute data of each JSON document produced by Perceval?

Data attribute is the data returned by the upstream API.

Thus JSON items returned by Prerceval contains 2 layers of information (meta information and the one that comes from remote repository).

Gitlab data attribute:
- Contains id, iid, project_id,title, description, state, created_at, updated_at, closed_at, closed_by, labels, milestone, assignees, author, assignee, user_notes_count, merge_requests_count, upvotes, downvotes, due_date, confidential, discussion_locked, web_url, time_stats, task_completion_status, weight, has_tasks, _links, references, moved_to_id, epic_iid, epic, notes_data, award_emoji_data.

Github data attribute:
- Contains url, repository_url, labels_url, comments_url, events_url, html_url, id, node_id, number,  title, user,  labels, state, locked, assignee, assignees, milestone, comments, created_at, updated_at, closed_at, author_association, pull_request, body, reactions, user_data,  assignee_data, assignees_data, comments_data, reactions_data.

***