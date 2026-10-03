"""Generated from Smithy shape ``com.amazonaws.guardduty#CreateTrustedEntitySetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.boolean
    import capo_guardduty.types.client_token
    import capo_guardduty.types.detector_id
    import capo_guardduty.types.expected_bucket_owner
    import capo_guardduty.types.location
    import capo_guardduty.types.name
    import capo_guardduty.types.tag_map
    import capo_guardduty.types.trusted_entity_set_format


class CreateTrustedEntitySetRequest(TypedDict, closed=True):
    detector_id: "capo_guardduty.types.detector_id.DetectorId"
    """<p>The unique ID of the detector of the GuardDuty account for which you want to create a trusted entity set.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>"""
    name: NotRequired["capo_guardduty.types.name.Name"]
    """<p>A user-friendly name to identify the trusted entity set.</p> <p>The name of your list can include lowercase letters, uppercase letters, numbers, dash (-), and underscore (_).</p>"""
    format: NotRequired[
        "capo_guardduty.types.trusted_entity_set_format.TrustedEntitySetFormat"
    ]
    """<p>The format of the file that contains the trusted entity set.</p>"""
    location: NotRequired["capo_guardduty.types.location.Location"]
    """<p>The URI of the file that contains the threat entity set. The format of the <code>Location</code> URL must be a valid Amazon S3 URL format. Invalid URL formats will result in an error, regardless of whether you activate the entity set or not. For more information about format of the location URLs, see <a href="https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-lists-create-activate.html">Format of location URL under Step 2: Adding trusted or threat intelligence data</a> in the <i>Amazon GuardDuty User Guide</i>.</p>"""
    expected_bucket_owner: NotRequired[
        "capo_guardduty.types.expected_bucket_owner.ExpectedBucketOwner"
    ]
    """<p>The Amazon Web Services account ID that owns the Amazon S3 bucket specified in the <b>location</b> parameter.</p>"""
    activate: NotRequired["capo_guardduty.types.boolean.Boolean"]
    """<p>A boolean value that indicates whether GuardDuty is to start using the uploaded trusted entity set.</p>"""
    client_token: NotRequired["capo_guardduty.types.client_token.ClientToken"]
    """<p>The idempotency token for the create request.</p>"""
    tags: NotRequired["capo_guardduty.types.tag_map.TagMap"]
    """<p>The tags to be added to a new trusted entity set resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTrustedEntitySetRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "format" in value:
        import capo_guardduty.types.trusted_entity_set_format

        out["format"] = capo_guardduty.types.trusted_entity_set_format.serialize_json(
            value["format"]
        )
    if "location" in value:
        out["location"] = value["location"]
    if "expected_bucket_owner" in value:
        out["expectedBucketOwner"] = value["expected_bucket_owner"]
    if "activate" in value:
        out["activate"] = value["activate"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import capo_guardduty.types.tag_map

        out["tags"] = capo_guardduty.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateTrustedEntitySetRequest:
    out: CreateTrustedEntitySetRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("format") is not None:
        import capo_guardduty.types.trusted_entity_set_format

        out["format"] = capo_guardduty.types.trusted_entity_set_format.deserialize_json(
            data["format"]
        )
    if data.get("location") is not None:
        out["location"] = data["location"]
    if data.get("expectedBucketOwner") is not None:
        out["expected_bucket_owner"] = data["expectedBucketOwner"]
    if data.get("activate") is not None:
        out["activate"] = data["activate"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("tags") is not None:
        import capo_guardduty.types.tag_map

        out["tags"] = capo_guardduty.types.tag_map.deserialize_json(data["tags"])
    return out
