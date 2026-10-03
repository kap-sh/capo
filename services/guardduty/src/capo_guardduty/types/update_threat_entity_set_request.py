"""Generated from Smithy shape ``com.amazonaws.guardduty#UpdateThreatEntitySetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.boolean
    import capo_guardduty.types.detector_id
    import capo_guardduty.types.expected_bucket_owner
    import capo_guardduty.types.location
    import capo_guardduty.types.name
    import capo_guardduty.types.string


class UpdateThreatEntitySetRequest(TypedDict, closed=True):
    detector_id: "capo_guardduty.types.detector_id.DetectorId"
    """<p>The unique ID of the GuardDuty detector associated with the threat entity set that you want to update.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>"""
    threat_entity_set_id: NotRequired["capo_guardduty.types.string.String"]
    """<p>The ID returned by GuardDuty after updating the threat entity set resource.</p>"""
    name: NotRequired["capo_guardduty.types.name.Name"]
    """<p>A user-friendly name to identify the trusted entity set.</p> <p>The name of your list can include lowercase letters, uppercase letters, numbers, dash (-), and underscore (_).</p>"""
    location: NotRequired["capo_guardduty.types.location.Location"]
    """<p>The URI of the file that contains the trusted entity set.</p>"""
    expected_bucket_owner: NotRequired[
        "capo_guardduty.types.expected_bucket_owner.ExpectedBucketOwner"
    ]
    """<p>The Amazon Web Services account ID that owns the Amazon S3 bucket specified in the <b>location</b> parameter.</p>"""
    activate: NotRequired["capo_guardduty.types.boolean.Boolean"]
    """<p>A boolean value that indicates whether GuardDuty is to start using this updated threat entity set. After you update an entity set, you will need to activate it again. It might take up to 15 minutes for the updated entity set to be effective.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateThreatEntitySetRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "location" in value:
        out["location"] = value["location"]
    if "expected_bucket_owner" in value:
        out["expectedBucketOwner"] = value["expected_bucket_owner"]
    if "activate" in value:
        out["activate"] = value["activate"]
    return out


def deserialize_json(data: dict) -> UpdateThreatEntitySetRequest:
    out: UpdateThreatEntitySetRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("location") is not None:
        out["location"] = data["location"]
    if data.get("expectedBucketOwner") is not None:
        out["expected_bucket_owner"] = data["expectedBucketOwner"]
    if data.get("activate") is not None:
        out["activate"] = data["activate"]
    return out
