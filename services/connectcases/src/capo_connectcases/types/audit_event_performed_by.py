"""Generated from Smithy shape ``com.amazonaws.connectcases#AuditEventPerformedBy``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.iam_principal_arn
    import capo_connectcases.types.user_union


class AuditEventPerformedBy(TypedDict, closed=True):
    user: NotRequired["capo_connectcases.types.user_union.UserUnion"]
    iam_principal_arn: "capo_connectcases.types.iam_principal_arn.IamPrincipalArn"
    """<p>Unique identifier of an IAM role.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuditEventPerformedBy) -> dict:
    out: dict = {}
    if "user" in value:
        import capo_connectcases.types.user_union

        out["user"] = capo_connectcases.types.user_union.serialize_json(value["user"])
    out["iamPrincipalArn"] = value["iam_principal_arn"]
    return out


def deserialize_json(data: dict) -> AuditEventPerformedBy:
    out: AuditEventPerformedBy = {}  # type: ignore[typeddict-item]
    if data.get("user") is not None:
        import capo_connectcases.types.user_union

        out["user"] = capo_connectcases.types.user_union.deserialize_json(data["user"])
    if data.get("iamPrincipalArn") is not None:
        out["iam_principal_arn"] = data["iamPrincipalArn"]
    else:
        out["iam_principal_arn"] = ""
    return out


def redact_sensitive(value: AuditEventPerformedBy) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "user" in value:
        import capo_connectcases.types.user_union

        out["user"] = capo_connectcases.types.user_union.redact_sensitive(value["user"])
    return out
