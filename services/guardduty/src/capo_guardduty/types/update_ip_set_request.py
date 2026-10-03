"""Generated from Smithy shape ``com.amazonaws.guardduty#UpdateIPSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.account_id
    import capo_guardduty.types.boolean
    import capo_guardduty.types.detector_id
    import capo_guardduty.types.location
    import capo_guardduty.types.name
    import capo_guardduty.types.string


class UpdateIPSetRequest(TypedDict, closed=True):
    detector_id: "capo_guardduty.types.detector_id.DetectorId"
    """<p>The detectorID that specifies the GuardDuty service whose IPSet you want to update.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>"""
    ip_set_id: NotRequired["capo_guardduty.types.string.String"]
    """<p>The unique ID that specifies the IPSet that you want to update.</p>"""
    name: NotRequired["capo_guardduty.types.name.Name"]
    """<p>The unique ID that specifies the IPSet that you want to update.</p>"""
    location: NotRequired["capo_guardduty.types.location.Location"]
    """<p>The updated URI of the file that contains the IPSet. </p>"""
    activate: NotRequired["capo_guardduty.types.boolean.Boolean"]
    """<p>The updated Boolean value that specifies whether the IPSet is active or not.</p>"""
    expected_bucket_owner: NotRequired["capo_guardduty.types.account_id.AccountId"]
    """<p>The Amazon Web Services account ID that owns the Amazon S3 bucket specified in the <b>location</b> parameter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateIPSetRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "location" in value:
        out["location"] = value["location"]
    if "activate" in value:
        out["activate"] = value["activate"]
    if "expected_bucket_owner" in value:
        out["expectedBucketOwner"] = value["expected_bucket_owner"]
    return out


def deserialize_json(data: dict) -> UpdateIPSetRequest:
    out: UpdateIPSetRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("location") is not None:
        out["location"] = data["location"]
    if data.get("activate") is not None:
        out["activate"] = data["activate"]
    if data.get("expectedBucketOwner") is not None:
        out["expected_bucket_owner"] = data["expectedBucketOwner"]
    return out
