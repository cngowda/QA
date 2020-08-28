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
        
2. #### _FT JOBS_
   1. [Identity API FT TEST](https://jenkins-cicd-staging.inca.infoblox.com/view/Athena_QA/job/Identity_API_FT_TEST/)
      > **_Repository_** [qa_xaas](https://github.com/Infoblox-CTO/qa-xaas/tree/portunus-athena-api)
      - from QA_XASS repository includes FT jobs for Identity
   
   2. [Hostapp API FT](https://jenkins-cicd-staging.inca.infoblox.com/view/Athena_QA/job/Hostapp_API_FT/)
      > **_Repository_** [qa_xaas](https://github.com/Infoblox-CTO/qa-xaas/tree/portunus-athena-api)
      - from QA_XASS repository includes FT jobs for Hostapp
      
   3. [SSO API FT Job](https://jenkins-cicd-staging.inca.infoblox.com/view/Athena_QA/job/SSO_API_FT_Job/)
      > **_Repository_** [qa_xaas](https://github.com/Infoblox-CTO/qa-xaas/tree/portunus-athena-api)
      - from QA_XASS repository includes FT jobs for SSO
   
   4. [Athena Identity FT](https://jenkins-cicd-staging.inca.infoblox.com/view/Athena_QA/job/Athena_Identity_FT/)
      > **_Repository_** [Athena_qa](https://github.com/Infoblox-CTO/athena_qa)
      - from athena qa repository includes FT jobs for Identity
   
   5. [AuthZ](https://jenkins-cicd-staging.inca.infoblox.com/view/Athena_QA/job/AuthZ/)
      > **_Repository_** [Athena_qa](https://github.com/Infoblox-CTO/athena_qa)
      - from athena qa repository includes FT jobs for AuthZ

## __UI JOBS__
1. #### _BVT JOBS_
   1. [BVT CSP PROD](https://jenkins-cicd-staging.inca.infoblox.com/view/Athena_QA/job/BVT_CSP_PROD/)
      > **_Repository_** [qa_xaas](https://github.com/Infoblox-CTO/qa-xaas/tree/portunus-athena-api)
      - from QA_XASS repository includes UI BVT pipline job includes Navigation to App specific pages
      - and test of basic crud operations on UI
         - Athena
         - Northstar
         
   1. [Athena UI FT](https://jenkins-cicd-staging.inca.infoblox.com/view/Athena_QA/job/Athena_UI_FT/)
      > **_Repository_** [qa_xaas](https://github.com/Infoblox-CTO/qa-xaas/tree/portunus-athena-api)
      - from QA_XASS repository includes UI FT job includes functional test for Athena pages
      - Pages included are
         - On-prem Host Page
         - Joint Token Page
         - Users Page
         - Usesr groups page
         - User role page
         - Access Policy Page
         - Logs Page
         - Landing Page
         - Support new Page
         - License Entitelment Page
         - Login Page
         - Tags Page
         - User Preferences page


