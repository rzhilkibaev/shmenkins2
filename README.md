# shmenkins2
# Requirements
python 3.6, pipenv, npm

# How to build
`$ make init` this will install tools/dependencies locally (into `node_modules` and virtualenv).

`$ make deploy` to deploy to AWS.

# Notes
Everything is an artifact group (ag): jar(s), test report, running service, VPN...
Every artifact has a dependency. There are multiple types of dependencies: source code, ag, approval...
Dependencies are also artifact groups. For example a source code repo is an artifact group.
Modeling a source code repo as a separate artifact group allows us to have an object for each source code repo.
We can attach additional info to that object and track it separately. Just like it is a separate object in real life.
If we use source code repo url just as a property of a jar artifact then we loose the ability to track
a source code repo as a separate object.

When an ag changes it makes all it's downstream dependencies outdated.

Each ag has one (?) build script that defines how the ag is built.
It lists all dependencies and artifacts (imports and exports).

# High level overview

Sequence of events:
 0. HandlePushNotification (UpdateSrc) lambda. A notification received from scm and an `artifact-updated` event is sent to `artifact-updated-q` queue.
 0. OutdateDownstreamArtifacts lambda. The `artifact-updated` event is received, a list of downstream dependencies is made and for each an `artifact-outdated` event is sent to `artifact-outdated-q` queue.
 0. ScheduleArtifactUpdate lambda. The `artifact-outdated` event is received and a build is scheduled (a `build-scheduled` event is sent to sqs).
 0. StartArtifactUpdate lambda. The `build-scheduled` event is received, a build is started and `build-started` event is sent to sqs/sns.
 0. CodeBuild project. The build is executed and a `build-finished` event is sent to sns.
 0. UpdateArtifact lambda. The `build-finished` event is received and an `artifact-updated` event is sent to `artifact-updated-q` queue.
 0. repeat.
