"""Generated from Smithy shape ``com.amazonaws.macie2#SearchResourcesSimpleCriterion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__list_of__string
    import capo_macie2.types.search_resources_comparator
    import capo_macie2.types.search_resources_simple_criterion_key


class SearchResourcesSimpleCriterion(TypedDict, closed=True):
    comparator: NotRequired[
        "capo_macie2.types.search_resources_comparator.SearchResourcesComparator"
    ]
    """<p>The operator to use in the condition. Valid values are EQ (equals) and NE (not equals).</p>"""
    key: NotRequired[
        "capo_macie2.types.search_resources_simple_criterion_key.SearchResourcesSimpleCriterionKey"
    ]
    """<p>The property to use in the condition.</p>"""
    values: NotRequired["capo_macie2.types.__list_of__string.__listOf__string"]
    """<p>An array that lists one or more values to use in the condition. If you specify multiple values, Amazon Macie uses OR logic to join the values. Valid values for each supported property (key) are:</p> <ul><li><p>ACCOUNT_ID - A string that represents the unique identifier for the Amazon Web Services account that owns the resource.</p></li> <li><p>AUTOMATED_DISCOVERY_MONITORING_STATUS - A string that represents an enumerated value that Macie defines for the <a href="https://docs.aws.amazon.com/macie/latest/APIReference/datasources-s3.html#datasources-s3-prop-bucketmetadata-automateddiscoverymonitoringstatus">BucketMetadata.automatedDiscoveryMonitoringStatus</a> property of an S3 bucket.</p></li> <li><p>S3_BUCKET_EFFECTIVE_PERMISSION - A string that represents an enumerated value that Macie defines for the <a href="https://docs.aws.amazon.com/macie/latest/APIReference/datasources-s3.html#datasources-s3-prop-bucketpublicaccess-effectivepermission">BucketPublicAccess.effectivePermission</a> property of an S3 bucket.</p></li> <li><p>S3_BUCKET_NAME - A string that represents the name of an S3 bucket.</p></li> <li><p>S3_BUCKET_SHARED_ACCESS - A string that represents an enumerated value that Macie defines for the <a href="https://docs.aws.amazon.com/macie/latest/APIReference/datasources-s3.html#datasources-s3-prop-bucketmetadata-sharedaccess">BucketMetadata.sharedAccess</a> property of an S3 bucket.</p></li></ul> <p>Values are case sensitive. Also, Macie doesn't support use of partial values or wildcard characters in values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchResourcesSimpleCriterion) -> dict:
    out: dict = {}
    if "comparator" in value:
        import capo_macie2.types.search_resources_comparator

        out["comparator"] = (
            capo_macie2.types.search_resources_comparator.serialize_json(
                value["comparator"]
            )
        )
    if "key" in value:
        import capo_macie2.types.search_resources_simple_criterion_key

        out["key"] = (
            capo_macie2.types.search_resources_simple_criterion_key.serialize_json(
                value["key"]
            )
        )
    if "values" in value:
        import capo_macie2.types.__list_of__string

        out["values"] = capo_macie2.types.__list_of__string.serialize_json(
            value["values"]
        )
    return out


def deserialize_json(data: dict) -> SearchResourcesSimpleCriterion:
    out: SearchResourcesSimpleCriterion = {}  # type: ignore[typeddict-item]
    if data.get("comparator") is not None:
        import capo_macie2.types.search_resources_comparator

        out["comparator"] = (
            capo_macie2.types.search_resources_comparator.deserialize_json(
                data["comparator"]
            )
        )
    if data.get("key") is not None:
        import capo_macie2.types.search_resources_simple_criterion_key

        out["key"] = (
            capo_macie2.types.search_resources_simple_criterion_key.deserialize_json(
                data["key"]
            )
        )
    if data.get("values") is not None:
        import capo_macie2.types.__list_of__string

        out["values"] = capo_macie2.types.__list_of__string.deserialize_json(
            data["values"]
        )
    return out
