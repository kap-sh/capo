"""Generated from Smithy shape ``com.amazonaws.ec2#GetImageFindingsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.get_image_findings_entry_set
    import capo_ec2.types.string


class GetImageFindingsResult(TypedDict, closed=True):
    image_findings: NotRequired[
        "capo_ec2.types.get_image_findings_entry_set.GetImageFindingsEntrySet"
    ]
    """<p>The Amazon Inspector findings for the AMI.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetImageFindingsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "image_findings" in value:
        import capo_ec2.types.get_image_findings_entry_set

        capo_ec2.types.get_image_findings_entry_set.serialize_ec2_query(
            value["image_findings"], pairs, f"{key_prefix}ImageFindingSet"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> GetImageFindingsResult:
    out: GetImageFindingsResult = {}  # type: ignore[typeddict-item]
    child_image_findings = el.find("imageFindingSet")
    if child_image_findings is not None:
        import capo_ec2.types.get_image_findings_entry_set

        out["image_findings"] = (
            capo_ec2.types.get_image_findings_entry_set.deserialize_ec2_query(
                child_image_findings
            )
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
