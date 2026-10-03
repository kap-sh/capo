"""Generated from Smithy shape ``com.amazonaws.guardduty#CreateIPSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.account_id
    import capo_guardduty.types.boolean
    import capo_guardduty.types.client_token
    import capo_guardduty.types.detector_id
    import capo_guardduty.types.ip_set_format
    import capo_guardduty.types.location
    import capo_guardduty.types.name
    import capo_guardduty.types.tag_map


class CreateIPSetRequest(TypedDict, closed=True):
    detector_id: "capo_guardduty.types.detector_id.DetectorId"
    """<p>The unique ID of the detector of the GuardDuty account for which you want to create an IPSet.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>"""
    name: NotRequired["capo_guardduty.types.name.Name"]
    """<p>The user-friendly name to identify the IPSet.</p> <p> Allowed characters are alphanumeric, whitespace, dash (-), and underscores (_).</p>"""
    format: NotRequired["capo_guardduty.types.ip_set_format.IpSetFormat"]
    """<p>The format of the file that contains the IPSet.</p>"""
    location: NotRequired["capo_guardduty.types.location.Location"]
    """<p>The URI of the file that contains the IPSet. </p>"""
    activate: NotRequired["capo_guardduty.types.boolean.Boolean"]
    """<p>A Boolean value that indicates whether GuardDuty is to start using the uploaded IPSet.</p>"""
    client_token: NotRequired["capo_guardduty.types.client_token.ClientToken"]
    """<p>The idempotency token for the create request.</p>"""
    tags: NotRequired["capo_guardduty.types.tag_map.TagMap"]
    """<p>The tags to be added to a new IP set resource.</p>"""
    expected_bucket_owner: NotRequired["capo_guardduty.types.account_id.AccountId"]
    """<p>The Amazon Web Services account ID that owns the Amazon S3 bucket specified in the <b>location</b> parameter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateIPSetRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "format" in value:
        import capo_guardduty.types.ip_set_format

        out["format"] = capo_guardduty.types.ip_set_format.serialize_json(
            value["format"]
        )
    if "location" in value:
        out["location"] = value["location"]
    if "activate" in value:
        out["activate"] = value["activate"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import capo_guardduty.types.tag_map

        out["tags"] = capo_guardduty.types.tag_map.serialize_json(value["tags"])
    if "expected_bucket_owner" in value:
        out["expectedBucketOwner"] = value["expected_bucket_owner"]
    return out


def deserialize_json(data: dict) -> CreateIPSetRequest:
    out: CreateIPSetRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("format") is not None:
        import capo_guardduty.types.ip_set_format

        out["format"] = capo_guardduty.types.ip_set_format.deserialize_json(
            data["format"]
        )
    if data.get("location") is not None:
        out["location"] = data["location"]
    if data.get("activate") is not None:
        out["activate"] = data["activate"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("tags") is not None:
        import capo_guardduty.types.tag_map

        out["tags"] = capo_guardduty.types.tag_map.deserialize_json(data["tags"])
    if data.get("expectedBucketOwner") is not None:
        out["expected_bucket_owner"] = data["expectedBucketOwner"]
    return out
