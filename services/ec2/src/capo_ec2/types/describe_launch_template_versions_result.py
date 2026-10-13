"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeLaunchTemplateVersionsResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.launch_template_version_set
    import capo_ec2.types.string


class DescribeLaunchTemplateVersionsResult(TypedDict, closed=True):
    launch_template_versions: NotRequired[
        "capo_ec2.types.launch_template_version_set.LaunchTemplateVersionSet"
    ]
    """<p>Information about the launch template versions.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeLaunchTemplateVersionsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "launch_template_versions" in value:
        import capo_ec2.types.launch_template_version_set

        capo_ec2.types.launch_template_version_set.serialize_ec2_query(
            value["launch_template_versions"],
            pairs,
            f"{key_prefix}LaunchTemplateVersionSet",
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeLaunchTemplateVersionsResult:
    out: DescribeLaunchTemplateVersionsResult = {}  # type: ignore[typeddict-item]
    child_launch_template_versions = el.find("launchTemplateVersionSet")
    if child_launch_template_versions is not None:
        import capo_ec2.types.launch_template_version_set

        out["launch_template_versions"] = (
            capo_ec2.types.launch_template_version_set.deserialize_ec2_query(
                child_launch_template_versions
            )
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out


def redact_sensitive(value: DescribeLaunchTemplateVersionsResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "launch_template_versions" in value:
        import capo_ec2.types.launch_template_version_set

        out["launch_template_versions"] = (
            capo_ec2.types.launch_template_version_set.redact_sensitive(
                value["launch_template_versions"]
            )
        )
    return out
