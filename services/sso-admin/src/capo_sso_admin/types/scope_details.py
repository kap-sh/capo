"""Generated from Smithy shape ``com.amazonaws.ssoadmin#ScopeDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sso_admin.types.scope
    import capo_sso_admin.types.scope_targets


class ScopeDetails(TypedDict, closed=True):
    scope: "capo_sso_admin.types.scope.Scope"
    """<p>The name of the access scope.</p>"""
    authorized_targets: NotRequired["capo_sso_admin.types.scope_targets.ScopeTargets"]
    """<p>An array list of ARNs of applications.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScopeDetails) -> dict:
    out: dict = {}
    out["Scope"] = value["scope"]
    if "authorized_targets" in value:
        import capo_sso_admin.types.scope_targets

        out["AuthorizedTargets"] = (
            capo_sso_admin.types.scope_targets.serialize_aws_json_1_1(
                value["authorized_targets"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ScopeDetails:
    out: ScopeDetails = {}  # type: ignore[typeddict-item]
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
    return out
