import requests
import configparser
import json

cfg = configparser.ConfigParser()
cfg.read("config.ini")
_api_url = str(cfg["default"]["api_url"])


def test_push_notification_accepted():
    response = requests.post(f"{_api_url}/push-notifications", data=get_push_notification_request_body())
    assert response.status_code == 201


def get_push_notification_request_body():
    return json.dumps({
        "ref": "refs/heads/master",
        "before": "94de77055247ff0dc03b055df044f66a7df316b6",
        "after": "dec32ce511ee88448e38845dbb77e5af1b200bc2",
        "created": False,
        "deleted": False,
        "forced": False,
        "base_ref": None,
        "compare": "https://github.com/bob/demo-simple-web/compare/94de77055247...dec32ce511ee",
        "commits": [
            {
                "id": "dec32ce511ee88448e38845dbb77e5af1b200bc2",
                "tree_id": "d0f496ba7776ea6f28b9d77c5634aba11088991d",
                "distinct": True,
                "message": "Remove IT (testig shmenkins)",
                "timestamp": "2017-03-10T14:12:21-08:00",
                "url": "https://github.com/bob/demo-simple-web/commit/dec32ce511ee88448e38845dbb77e5af1b200bc2",
                "author": {
                    "name": "Renat",
                    "email": "xxxxxxxxxxxxxxxxxxxx"
                },
                "committer": {
                    "name": "Renat",
                    "email": "xxxxxxxxxxxxxxxxxxxx"
                },
                "added": [
                ],
                "removed": [
                    "demo-store/src/test/java/org/simplemart/product/ProductSmokeIT.java"
                ],
                "modified": [
                ]
            }
        ],
        "head_commit": {
            "id": "dec32ce511ee88448e38845dbb77e5af1b200bc2",
            "tree_id": "d0f496ba7776ea6f28b9d77c5634aba11088991d",
            "distinct": True,
            "message": "Remove IT (testig shmenkins)",
            "timestamp": "2017-03-10T14:12:21-08:00",
            "url": "https://github.com/bob/demo-simple-web/commit/dec32ce511ee88448e38845dbb77e5af1b200bc2",
            "author": {
                "name": "Renat",
                "email": "xxx"
            },
            "committer": {
                "name": "Renat",
                "email": "xxx"
            },
            "added": [
            ],
            "removed": [
                "demo-store/src/test/java/org/simplemart/product/ProductSmokeIT.java"
            ],
            "modified": [
            ]
        },
        "repository": {
            "id": 13280002,
            "name": "demo-simple-web",
            "full_name": "bob/demo-simple-web",
            "owner": {
                "name": "bob",
                "email": "bob@users.noreply.github.com",
                "login": "bob",
                "id": 3160853,
                "avatar_url": "https://avatars1.githubusercontent.com/u/3160853?v=3",
                "gravatar_id": "",
                "url": "https://api.github.com/users/bob",
                "html_url": "https://github.com/bob",
                "followers_url": "https://api.github.com/users/bob/followers",
                "following_url": "https://api.github.com/users/bob/following{/other_user}",
                "gists_url": "https://api.github.com/users/bob/gists{/gist_id}",
                "starred_url": "https://api.github.com/users/bob/starred{/owner}{/repo}",
                "subscriptions_url": "https://api.github.com/users/bob/subscriptions",
                "organizations_url": "https://api.github.com/users/bob/orgs",
                "repos_url": "https://api.github.com/users/bob/repos",
                "events_url": "https://api.github.com/users/bob/events{/privacy}",
                "received_events_url": "https://api.github.com/users/bob/received_events",
                "type": "User",
                "site_admin": False
            },
            "private": False,
            "html_url": "https://github.com/bob/demo-simple-web",
            "description": "Simple desktop web app demo",
            "fork": False,
            "url": "https://github.com/bob/demo-simple-web",
            "forks_url": "https://api.github.com/repos/bob/demo-simple-web/forks",
            "keys_url": "https://api.github.com/repos/bob/demo-simple-web/keys{/key_id}",
            "collaborators_url": "https://api.github.com/repos/bob/demo-simple-web/collaborators{/collaborator}",
            "teams_url": "https://api.github.com/repos/bob/demo-simple-web/teams",
            "hooks_url": "https://api.github.com/repos/bob/demo-simple-web/hooks",
            "issue_events_url": "https://api.github.com/repos/bob/demo-simple-web/issues/events{/number}",
            "events_url": "https://api.github.com/repos/bob/demo-simple-web/events",
            "assignees_url": "https://api.github.com/repos/bob/demo-simple-web/assignees{/user}",
            "branches_url": "https://api.github.com/repos/bob/demo-simple-web/branches{/branch}",
            "tags_url": "https://api.github.com/repos/bob/demo-simple-web/tags",
            "blobs_url": "https://api.github.com/repos/bob/demo-simple-web/git/blobs{/sha}",
            "git_tags_url": "https://api.github.com/repos/bob/demo-simple-web/git/tags{/sha}",
            "git_refs_url": "https://api.github.com/repos/bob/demo-simple-web/git/refs{/sha}",
            "trees_url": "https://api.github.com/repos/bob/demo-simple-web/git/trees{/sha}",
            "statuses_url": "https://api.github.com/repos/bob/demo-simple-web/statuses/{sha}",
            "languages_url": "https://api.github.com/repos/bob/demo-simple-web/languages",
            "stargazers_url": "https://api.github.com/repos/bob/demo-simple-web/stargazers",
            "contributors_url": "https://api.github.com/repos/bob/demo-simple-web/contributors",
            "subscribers_url": "https://api.github.com/repos/bob/demo-simple-web/subscribers",
            "subscription_url": "https://api.github.com/repos/bob/demo-simple-web/subscription",
            "commits_url": "https://api.github.com/repos/bob/demo-simple-web/commits{/sha}",
            "git_commits_url": "https://api.github.com/repos/bob/demo-simple-web/git/commits{/sha}",
            "comments_url": "https://api.github.com/repos/bob/demo-simple-web/comments{/number}",
            "issue_comment_url": "https://api.github.com/repos/bob/demo-simple-web/issues/comments{/number}",
            "contents_url": "https://api.github.com/repos/bob/demo-simple-web/contents/{+path}",
            "compare_url": "https://api.github.com/repos/bob/demo-simple-web/compare/{base}...{head}",
            "merges_url": "https://api.github.com/repos/bob/demo-simple-web/merges",
            "archive_url": "https://api.github.com/repos/bob/demo-simple-web/{archive_format}{/ref}",
            "downloads_url": "https://api.github.com/repos/bob/demo-simple-web/downloads",
            "issues_url": "https://api.github.com/repos/bob/demo-simple-web/issues{/number}",
            "pulls_url": "https://api.github.com/repos/bob/demo-simple-web/pulls{/number}",
            "milestones_url": "https://api.github.com/repos/bob/demo-simple-web/milestones{/number}",
            "notifications_url": "https://api.github.com/repos/bob/demo-simple-web/notifications{?since,all,participating}",
            "labels_url": "https://api.github.com/repos/bob/demo-simple-web/labels{/name}",
            "releases_url": "https://api.github.com/repos/bob/demo-simple-web/releases{/id}",
            "deployments_url": "https://api.github.com/repos/bob/demo-simple-web/deployments",
            "created_at": 1380740327,
            "updated_at": "2016-08-14T22:17:46Z",
            "pushed_at": 1489183948,
            "git_url": "git://github.com/bob/demo-simple-web.git",
            "ssh_url": "git@github.com:bob/demo-simple-web.git",
            "clone_url": "https://github.com/bob/demo-simple-web.git",
            "svn_url": "https://github.com/bob/demo-simple-web",
            "homepage": None,
            "size": 32,
            "stargazers_count": 0,
            "watchers_count": 0,
            "language": "Java",
            "has_issues": True,
            "has_downloads": True,
            "has_wiki": True,
            "has_pages": False,
            "forks_count": 0,
            "mirror_url": None,
            "open_issues_count": 0,
            "forks": 0,
            "open_issues": 0,
            "watchers": 0,
            "default_branch": "master",
            "stargazers": 0,
            "master_branch": "master"
        },
        "pusher": {
            "name": "bob",
            "email": "bob@users.noreply.github.com"
        },
        "sender": {
            "login": "bob",
            "id": 3160853,
            "avatar_url": "https://avatars1.githubusercontent.com/u/3160853?v=3",
            "gravatar_id": "",
            "url": "https://api.github.com/users/bob",
            "html_url": "https://github.com/bob",
            "followers_url": "https://api.github.com/users/bob/followers",
            "following_url": "https://api.github.com/users/bob/following{/other_user}",
            "gists_url": "https://api.github.com/users/bob/gists{/gist_id}",
            "starred_url": "https://api.github.com/users/bob/starred{/owner}{/repo}",
            "subscriptions_url": "https://api.github.com/users/bob/subscriptions",
            "organizations_url": "https://api.github.com/users/bob/orgs",
            "repos_url": "https://api.github.com/users/bob/repos",
            "events_url": "https://api.github.com/users/bob/events{/privacy}",
            "received_events_url": "https://api.github.com/users/bob/received_events",
            "type": "User",
            "site_admin": False
        }
    })
