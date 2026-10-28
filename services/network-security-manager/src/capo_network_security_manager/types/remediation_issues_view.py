"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#RemediationIssuesView``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_network_security_manager.errors import (
    DeserializationError,
    SerializationError,
)
from capo_network_security_manager.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_network_security_manager.types.not_visible_marker
    import capo_network_security_manager.types.remediation_issues


class RemediationIssuesViewIssuesMember(TypedDict, closed=True):
    issues: "capo_network_security_manager.types.remediation_issues.RemediationIssues"


class RemediationIssuesViewNotVisibleMember(TypedDict, closed=True):
    notVisible: (
        "capo_network_security_manager.types.not_visible_marker.NotVisibleMarker"
    )


RemediationIssuesView: TypeAlias = (
    RemediationIssuesViewIssuesMember
    | RemediationIssuesViewNotVisibleMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: RemediationIssuesView) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"RemediationIssuesView: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "issues" in value:
        import capo_network_security_manager.types.remediation_issues

        return {
            "issues": capo_network_security_manager.types.remediation_issues.serialize_json(
                value["issues"]
            )
        }
    elif "notVisible" in value:
        import capo_network_security_manager.types.not_visible_marker

        return {
            "notVisible": capo_network_security_manager.types.not_visible_marker.serialize_json(
                value["notVisible"]
            )
        }
    else:
        raise SerializationError("RemediationIssuesView: no variant present")


def deserialize_json(data: dict) -> RemediationIssuesView:
    if data.get("issues") is not None:
        import capo_network_security_manager.types.remediation_issues

        return {
            "issues": capo_network_security_manager.types.remediation_issues.deserialize_json(
                data["issues"]
            )
        }
    elif data.get("notVisible") is not None:
        import capo_network_security_manager.types.not_visible_marker

        return {
            "notVisible": capo_network_security_manager.types.not_visible_marker.deserialize_json(
                data["notVisible"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("RemediationIssuesView: no recognized variant key")
