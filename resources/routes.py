from resources.auth import Register, Login
from resources.complaint import (
    ListCreateComplaint,
    CompalaintDetail,
    ApproveComplaint,
    RejectComplaint,
)

routes = (
    (Register, "/register"),
    (Login, "/login"),
    (ListCreateComplaint, "/complainers/complaints"),
    (CompalaintDetail, "/complainers/complaints/<int:id_>"),
    (ApproveComplaint, "/approvers/complaints/<int:id_>/approve"),
    (RejectComplaint, "/approvers/complaints/<int:id_>/reject"),
)
