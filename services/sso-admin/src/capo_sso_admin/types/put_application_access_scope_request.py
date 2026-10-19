"""Generated from Smithy shape ``com.amazonaws.ssoadmin#PutApplicationAccessScopeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sso_admin.types.application_arn
    import capo_sso_admin.types.scope
    import capo_sso_admin.types.scope_targets


class PutApplicationAccessScopeRequest(TypedDict, closed=True):
    scope: "capo_sso_admin.types.scope.Scope"
    """<p>Specifies the name of the access scope to be associated with the specified targets.</p>"""
    authorized_targets: NotRequired["capo_sso_admin.types.scope_targets.ScopeTargets"]
    """<p>Specifies an array list of ARNs that represent the authorized targets for this access scope.</p>"""
    application_arn: "capo_sso_admin.types.application_arn.ApplicationArn"
    """<p>Specifies the ARN of the application with the access scope with the targets to add or update.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutApplicationAccessScopeRequest) -> dict:
    out: dict = {}
    out["Scope"] = value["scope"]
    if "authorized_targets" in value:
        import capo_sso_admin.types.scope_targets

        out["AuthorizedTargets"] = (
            capo_sso_admin.types.scope_targets.serialize_aws_json_1_1(
                value["authorized_targets"]
            )
        )
    out["ApplicationArn"] = value["application_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutApplicationAccessScopeRequest:
    out: PutApplicationAccessScopeRequest = {}  # type: ignore[typeddict-item]
    if data.get("Scope") is not None:
        out["scope"] = data["Scope"]
    else:
        out["scope"] = ""
    if data.get("AuthorizedTargets") is not None:
        import capo_sso_admin.types.scope_targets

        out["authorized_targets"] = (
            capo_sso_admin.types.scope_targets.deserialize_aws_json_1_1(
                data["AuthorizedTargets"]
            )
        )
    if data.get("ApplicationArn") is not None:
        out["application_arn"] = data["ApplicationArn"]
    else:
        out["application_arn"] = ""
    return out
