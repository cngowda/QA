# Athena Jenkins Jobs
###### _Jenkins Jobs relates to Athena qa_
![Jenkins](cool-jenkins.png)

## __API JOBS__

1. #### _BVT JOBS_
   1. [Athena BVT](https://jenkins-cicd-staging.inca.infoblox.com/view/Athena_QA/job/Athena_BVT/)
      > **_Repository_** [Athena_qa](https://github.com/Infoblox-CTO/athena_qa)
      - Pipline job includes BVT for Below items
        - Entitlment
        - Identity
        - hostapp
        
   2. [Athena BVT](https://jenkins-cicd-staging.inca.infoblox.com/view/Athena_QA/job/Athena_BVT_PR/)
      > **_Repository_** [Athena_qa](https://github.com/Infoblox-CTO/athena_qa)
      - Pipline job includes BVT for Below items, this job used after raising a PR to athena_qa repository
      '''
        - Entitlment
        - Identity
        - hostapp
       '''
   3. [Athena BVT_PR](https://jenkins-cicd-staging.inca.infoblox.com/view/Athena_QA/job/Athena_BVT_Job/)
      > **_Repository_** [qa_xaas](https://github.com/Infoblox-CTO/qa-xaas/tree/portunus-athena-api)
      - BVT from QA_XASS repository includes BVT for Below items
        - Entitlment
        - Identity
        - hostapp
      


