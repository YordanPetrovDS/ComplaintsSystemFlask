from resources.auth import Login, LoginApprover, Register
from resources.complaint import (
    ApproveComplaint,
    CompalaintDetail,
    ListCreateComplaint,
    RejectComplaint,
)

routes = (
    (Register, "/register"),
    (Login, "/login"),
    (LoginApprover, "/approvers/login"),
    (ListCreateComplaint, "/complainers/complaints"),
    (CompalaintDetail, "/complainers/complaints/<int:id_>"),
    (ApproveComplaint, "/approvers/complaints/<int:id_>/approve"),
    (RejectComplaint, "/approvers/complaints/<int:id_>/reject"),
)


# (RegisterComplainer, "/register"),
#     (LoginComplainer, "/login"),
#     (LoginApprover, "/approvers/login"),


#     (ComplaintListCreate, "/complainers/complaints"),
#     (CreateAdmin, "/admins/create-admin"),
#     (CreateApprover, "/admins/create-approver"),
#     (ComplaintManagement, "/admins/complains/<int:id_>"),
#     (LoginAdministrator, "/admins/login"),
