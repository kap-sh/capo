"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsS3BucketBucketLifecycleConfigurationRulesTransitionsDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.integer
    import capo_securityhub.types.non_empty_string


class AwsS3BucketBucketLifecycleConfigurationRulesTransitionsDetails(
    TypedDict, closed=True
):
    date: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>A date on which to transition objects to the specified storage class. If you provide <code>Date</code>, you cannot provide <code>Days</code>.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps">Timestamps</a>.</p>"""
    days: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The number of days after which to transition the object to the specified storage class. If you provide <code>Days</code>, you cannot provide <code>Date</code>.</p>"""
    storage_class: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The storage class to transition the object to. Valid values are as follows:</p> <ul> <li> <p> <code>DEEP_ARCHIVE</code> </p> </li> <li> <p> <code>GLACIER</code> </p> </li> <li> <p> <code>INTELLIGENT_TIERING</code> </p> </li> <li> <p> <code>ONEZONE_IA</code> </p> </li> <li> <p> <code>STANDARD_IA</code> </p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsS3BucketBucketLifecycleConfigurationRulesTransitionsDetails,
) -> dict:
    out: dict = {}
    if "date" in value:
        out["Date"] = value["date"]
    if "days" in value:
        out["Days"] = value["days"]
    if "storage_class" in value:
        out["StorageClass"] = value["storage_class"]
    return out


def deserialize_json(
    data: dict,
) -> AwsS3BucketBucketLifecycleConfigurationRulesTransitionsDetails:
    out: AwsS3BucketBucketLifecycleConfigurationRulesTransitionsDetails = {}  # type: ignore[typeddict-item]
    if data.get("Date") is not None:
        out["date"] = data["Date"]
    if data.get("Days") is not None:
        out["days"] = data["Days"]
    if data.get("StorageClass") is not None:
        out["storage_class"] = data["StorageClass"]
    return out
