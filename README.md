# DS-Lab9

## Before 10th step
![](https://i.imgur.com/AHSM0sN.png)

### rs.status()

```
{
        "set" : "rs0",
        "date" : ISODate("2019-11-01T20:20:26.760Z"),
        "myState" : 2,
        "term" : NumberLong(2),
        "syncingTo" : "vm3:27017",
        "syncSourceHost" : "vm3:27017",
        "syncSourceId" : 2,
        "heartbeatIntervalMillis" : NumberLong(2000),
        "majorityVoteCount" : 2,
        "writeMajorityCount" : 2,
        "optimes" : {
                "lastCommittedOpTime" : {
                        "ts" : Timestamp(1572639625, 1),
                        "t" : NumberLong(2)
                },
                "lastCommittedWallTime" : ISODate("2019-11-01T20:20:25.051Z"),
                "readConcernMajorityOpTime" : {
                        "ts" : Timestamp(1572639625, 1),
                        "t" : NumberLong(2)
                },
                "readConcernMajorityWallTime" : ISODate("2019-11-01T20:20:25.051Z"),
                "appliedOpTime" : {
                        "ts" : Timestamp(1572639625, 1),
                        "t" : NumberLong(2)
                },
                "durableOpTime" : {
                        "ts" : Timestamp(1572639625, 1),
                        "t" : NumberLong(2)
                },
                "lastAppliedWallTime" : ISODate("2019-11-01T20:20:25.051Z"),
                "lastDurableWallTime" : ISODate("2019-11-01T20:20:25.051Z")
        },
        "lastStableRecoveryTimestamp" : Timestamp(1572639615, 1),
        "lastStableCheckpointTimestamp" : Timestamp(1572639615, 1),
        "members" : [
                {
                        "_id" : 0,
                        "name" : "vm1:27017",
                        "ip" : "172.31.27.38",
                        "health" : 1,
                        "state" : 2,
                        "stateStr" : "SECONDARY",
                        "uptime" : 1149,
                        "optime" : {
                                "ts" : Timestamp(1572639625, 1),
                                "t" : NumberLong(2)
                        },
                        "optimeDate" : ISODate("2019-11-01T20:20:25Z"),
                        "syncingTo" : "vm3:27017",
                        "syncSourceHost" : "vm3:27017",
                        "syncSourceId" : 2,
                        "infoMessage" : "",
                        "configVersion" : 1,
                        "self" : true,
                        "lastHeartbeatMessage" : ""
                },
                {
                        "_id" : 1,
                        "name" : "vm2:27017",
                        "ip" : "172.31.39.117",
                        "health" : 1,
                        "state" : 1,
                        "stateStr" : "PRIMARY",
                        "uptime" : 1148,
                        "optime" : {
                                "ts" : Timestamp(1572639625, 1),
                                "t" : NumberLong(2)
                        },
                        "optimeDurable" : {
                                "ts" : Timestamp(1572639625, 1),
                                "t" : NumberLong(2)
                        },
                        "optimeDate" : ISODate("2019-11-01T20:20:25Z"),
                        "optimeDurableDate" : ISODate("2019-11-01T20:20:25Z"),
                        "lastHeartbeat" : ISODate("2019-11-01T20:20:26.322Z"),
                        "lastHeartbeatRecv" : ISODate("2019-11-01T20:20:25.654Z"),
                        "pingMs" : NumberLong(0),
                        "lastHeartbeatMessage" : "",
                        "syncingTo" : "",
                        "syncSourceHost" : "",
                        "syncSourceId" : -1,
                        "infoMessage" : "",
                        "electionTime" : Timestamp(1572637944, 1),
                        "electionDate" : ISODate("2019-11-01T19:52:24Z"),
                        "configVersion" : 1
                },
                {
                        "_id" : 2,
                        "name" : "vm3:27017",
                        "ip" : "172.31.42.78",
                        "health" : 1,
                        "state" : 2,
                        "stateStr" : "SECONDARY",
                        "uptime" : 1148,
                        "optime" : {
                                "ts" : Timestamp(1572639625, 1),
                                "t" : NumberLong(2)
                        },
                        "optimeDurable" : {
                                "ts" : Timestamp(1572639625, 1),
                                "t" : NumberLong(2)
                        },
                        "optimeDate" : ISODate("2019-11-01T20:20:25Z"),
                        "optimeDurableDate" : ISODate("2019-11-01T20:20:25Z"),
                        "lastHeartbeat" : ISODate("2019-11-01T20:20:26.322Z"),
                        "lastHeartbeatRecv" : ISODate("2019-11-01T20:20:25.087Z"),
                        "pingMs" : NumberLong(0),
                        "lastHeartbeatMessage" : "",
                        "syncingTo" : "vm2:27017",
                        "syncSourceHost" : "vm2:27017",
                        "syncSourceId" : 1,
                        "infoMessage" : "",
                        "configVersion" : 1
                }
        ],
        "ok" : 1,
        "$clusterTime" : {
                "clusterTime" : Timestamp(1572639625, 1),
                "signature" : {
                        "hash" : BinData(0,"AAAAAAAAAAAAAAAAAAAAAAAAAAA="),
                        "keyId" : NumberLong(0)
                }
        },
        "operationTime" : Timestamp(1572639625, 1)
}
```

### rs.config()
```
{
        "_id" : "rs0",
        "version" : 1,
        "protocolVersion" : NumberLong(1),
        "writeConcernMajorityJournalDefault" : true,
        "members" : [
                {
                        "_id" : 0,
                        "host" : "vm1:27017",
                        "arbiterOnly" : false,
                        "buildIndexes" : true,
                        "hidden" : false,
                        "priority" : 1,
                        "tags" : {

                        },
                        "slaveDelay" : NumberLong(0),
                        "votes" : 1
                },
                {
                        "_id" : 1,
                        "host" : "vm2:27017",
                        "arbiterOnly" : false,
                        "buildIndexes" : true,
                        "hidden" : false,
                        "priority" : 1,
                        "tags" : {

                        },
                        "slaveDelay" : NumberLong(0),
                        "votes" : 1
                },
                {
                        "_id" : 2,
                        "host" : "vm3:27017",
                        "arbiterOnly" : false,
                        "buildIndexes" : true,
                        "hidden" : false,
                        "priority" : 1,
                        "tags" : {

                        },
                        "slaveDelay" : NumberLong(0),
                        "votes" : 1
                }
        ],
        "settings" : {
                "chainingAllowed" : true,
                "heartbeatIntervalMillis" : 2000,
                "heartbeatTimeoutSecs" : 10,
                "electionTimeoutMillis" : 10000,
                "catchUpTimeoutMillis" : -1,
                "catchUpTakeoverDelayMillis" : 30000,
                "getLastErrorModes" : {

                },
                "getLastErrorDefaults" : {
                        "w" : 1,
                        "wtimeout" : 0
                },
                "replicaSetId" : ObjectId("5dbc8cb665887ac3dc4d630c")
        }
}
```


## 10th step

![](https://i.imgur.com/pZ4rcUI.png)

### rs.status()

```
{
        "set" : "rs0",
        "date" : ISODate("2019-11-01T20:32:16.344Z"),
        "myState" : 1,
        "term" : NumberLong(3),
        "syncingTo" : "",
        "syncSourceHost" : "",
        "syncSourceId" : -1,
        "heartbeatIntervalMillis" : NumberLong(2000),
        "majorityVoteCount" : 2,
        "writeMajorityCount" : 2,
        "optimes" : {
                "lastCommittedOpTime" : {
                        "ts" : Timestamp(1572640334, 1),
                        "t" : NumberLong(3)
                },
                "lastCommittedWallTime" : ISODate("2019-11-01T20:32:14.054Z"),
                "readConcernMajorityOpTime" : {
                        "ts" : Timestamp(1572640334, 1),
                        "t" : NumberLong(3)
                },
                "readConcernMajorityWallTime" : ISODate("2019-11-01T20:32:14.054Z"),
                "appliedOpTime" : {
                        "ts" : Timestamp(1572640334, 1),
                        "t" : NumberLong(3)
                },
                "durableOpTime" : {
                        "ts" : Timestamp(1572640334, 1),
                        "t" : NumberLong(3)
                },
                "lastAppliedWallTime" : ISODate("2019-11-01T20:32:14.054Z"),
                "lastDurableWallTime" : ISODate("2019-11-01T20:32:14.054Z")
        },
        "lastStableRecoveryTimestamp" : Timestamp(1572640278, 1),
        "lastStableCheckpointTimestamp" : Timestamp(1572640278, 1),
        "electionCandidateMetrics" : {
                "lastElectionReason" : "stepUpRequestSkipDryRun",
                "lastElectionDate" : ISODate("2019-11-01T20:25:02.962Z"),
                "termAtElection" : NumberLong(3),
                "lastCommittedOpTimeAtElection" : {
                        "ts" : Timestamp(1572639895, 1),
                        "t" : NumberLong(2)
                },
                "lastSeenOpTimeAtElection" : {
                        "ts" : Timestamp(1572639895, 1),
                        "t" : NumberLong(2)
                },
                "numVotesNeeded" : 2,
                "priorityAtElection" : 1,
                "electionTimeoutMillis" : NumberLong(10000),
                "priorPrimaryMemberId" : 1,
                "numCatchUpOps" : NumberLong(27017),
                "newTermStartDate" : ISODate("2019-11-01T20:25:04.042Z"),
                "wMajorityWriteAvailabilityDate" : ISODate("2019-11-01T20:25:04.858Z")
        },
        "members" : [
                {
                        "_id" : 0,
                        "name" : "vm1:27017",
                        "ip" : "172.31.27.38",
                        "health" : 1,
                        "state" : 1,
                        "stateStr" : "PRIMARY",
                        "uptime" : 1859,
                        "optime" : {
                                "ts" : Timestamp(1572640334, 1),
                                "t" : NumberLong(3)
                        },
                        "optimeDate" : ISODate("2019-11-01T20:32:14Z"),
                        "syncingTo" : "",
                        "syncSourceHost" : "",
                        "syncSourceId" : -1,
                        "infoMessage" : "",
                        "electionTime" : Timestamp(1572639902, 1),
                        "electionDate" : ISODate("2019-11-01T20:25:02Z"),
                        "configVersion" : 1,
                        "self" : true,
                        "lastHeartbeatMessage" : ""
                },
                {
                        "_id" : 1,
                        "name" : "vm2:27017",
                        "ip" : "172.31.39.117",
                        "health" : 0,
                        "state" : 8,
                        "stateStr" : "(not reachable/healthy)",
                        "uptime" : 0,
                        "optime" : {
                                "ts" : Timestamp(0, 0),
                                "t" : NumberLong(-1)
                        },
                        "optimeDurable" : {
                                "ts" : Timestamp(0, 0),
                                "t" : NumberLong(-1)
                        },
                        "optimeDate" : ISODate("1970-01-01T00:00:00Z"),
                        "optimeDurableDate" : ISODate("1970-01-01T00:00:00Z"),
                        "lastHeartbeat" : ISODate("2019-11-01T20:32:15.999Z"),
                        "lastHeartbeatRecv" : ISODate("2019-11-01T20:25:03.790Z"),
                        "pingMs" : NumberLong(0),
                        "lastHeartbeatMessage" : "Couldn't get a connection within the time limit",
                        "syncingTo" : "",
                        "syncSourceHost" : "",
                        "syncSourceId" : -1,
                        "infoMessage" : "",
                        "configVersion" : -1
                },
                {
                        "_id" : 2,
                        "name" : "vm3:27017",
                        "ip" : "172.31.42.78",
                        "health" : 1,
                        "state" : 2,
                        "stateStr" : "SECONDARY",
                        "uptime" : 1857,
                        "optime" : {
                                "ts" : Timestamp(1572640334, 1),
                                "t" : NumberLong(3)
                        },
                        "optimeDurable" : {
                                "ts" : Timestamp(1572640334, 1),
                                "t" : NumberLong(3)
                        },
                        "optimeDate" : ISODate("2019-11-01T20:32:14Z"),
                        "optimeDurableDate" : ISODate("2019-11-01T20:32:14Z"),
                        "lastHeartbeat" : ISODate("2019-11-01T20:32:15.183Z"),
                        "lastHeartbeatRecv" : ISODate("2019-11-01T20:32:15.068Z"),
                        "pingMs" : NumberLong(0),
                        "lastHeartbeatMessage" : "",
                        "syncingTo" : "vm1:27017",
                        "syncSourceHost" : "vm1:27017",
                        "syncSourceId" : 0,
                        "infoMessage" : "",
                        "configVersion" : 1
                }
        ],
        "ok" : 1,
        "$clusterTime" : {
                "clusterTime" : Timestamp(1572640334, 1),
                "signature" : {
                        "hash" : BinData(0,"AAAAAAAAAAAAAAAAAAAAAAAAAAA="),
                        "keyId" : NumberLong(0)
                }
        },
        "operationTime" : Timestamp(1572640334, 1)
}
```


### rs.config()

```
{
        "_id" : "rs0",
        "version" : 1,
        "protocolVersion" : NumberLong(1),
        "writeConcernMajorityJournalDefault" : true,
        "members" : [
                {
                        "_id" : 0,
                        "host" : "vm1:27017",
                        "arbiterOnly" : false,
                        "buildIndexes" : true,
                        "hidden" : false,
                        "priority" : 1,
                        "tags" : {

                        },
                        "slaveDelay" : NumberLong(0),
                        "votes" : 1
                },
                {
                        "_id" : 1,
                        "host" : "vm2:27017",
                        "arbiterOnly" : false,
                        "buildIndexes" : true,
                        "hidden" : false,
                        "priority" : 1,
                        "tags" : {

                        },
                        "slaveDelay" : NumberLong(0),
                        "votes" : 1
                },
                {
                        "_id" : 2,
                        "host" : "vm3:27017",
                        "arbiterOnly" : false,
                        "buildIndexes" : true,
                        "hidden" : false,
                        "priority" : 1,
                        "tags" : {

                        },
                        "slaveDelay" : NumberLong(0),
                        "votes" : 1
                }
        ],
        "settings" : {
                "chainingAllowed" : true,
                "heartbeatIntervalMillis" : 2000,
                "heartbeatTimeoutSecs" : 10,
                "electionTimeoutMillis" : 10000,
                "catchUpTimeoutMillis" : -1,
                "catchUpTakeoverDelayMillis" : 30000,
                "getLastErrorModes" : {

                },
                "getLastErrorDefaults" : {
                        "w" : 1,
                        "wtimeout" : 0
                },
                "replicaSetId" : ObjectId("5dbc8cb665887ac3dc4d630c")
        }
}
```

## Sources
https://codeburst.io/building-your-first-chat-application-using-flask-in-7-minutes-f98de4adfa5d
