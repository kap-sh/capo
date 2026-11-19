"""Generated from Smithy shape ``com.amazonaws.codebuild#ProjectBadge``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.boolean
    import capo_codebuild.types.string


class ProjectBadge(TypedDict, closed=True):
    badge_enabled: "capo_codebuild.types.boolean.Boolean"
    """<p>Set this to true to generate a publicly accessible URL for your project's build badge.</p>"""
    badge_request_url: NotRequired["capo_codebuild.types.string.String"]
    """<p>The publicly-accessible URL through which you can access the build badge for your project. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProjectBadge) -> dict:
    out: dict = {}
    out["badgeEnabled"] = value.get("badge_enabled", False)
    if "badge_request_url" in value:
        out["badgeRequestUrl"] = value["badge_request_url"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ProjectBadge:
    out: ProjectBadge = {}  # type: ignore[typeddict-item]
    if data.get("badgeEnabled") is not None:
        out["badge_enabled"] = data["badgeEnabled"]
    else:
        out["badge_enabled"] = False
    if data.get("badgeRequestUrl") is not None:
        out["badge_request_url"] = data["badgeRequestUrl"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ProjectBadge) -> dict:
    out: dict = {}
    out["badgeEnabled"] = value.get("badge_enabled", False)
    if "badge_request_url" in value:
        out["badgeRequestUrl"] = value["badge_request_url"]
    return out


def deserialize_cbor(data: dict) -> ProjectBadge:
    out: ProjectBadge = {}  # type: ignore[typeddict-item]
    if data.get("badgeEnabled") is not None:
        out["badge_enabled"] = data["badgeEnabled"]
    else:
        out["badge_enabled"] = False
    if data.get("badgeRequestUrl") is not None:
        out["badge_request_url"] = data["badgeRequestUrl"]
    return out
