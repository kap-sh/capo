"""Generated from Smithy shape ``com.amazonaws.customerprofiles#UpdateDomainRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.data_store_request
    import capo_customer_profiles.types.encryption_key
    import capo_customer_profiles.types.expiration_days_integer
    import capo_customer_profiles.types.matching_request
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.rule_based_matching_request
    import capo_customer_profiles.types.sqs_queue_url
    import capo_customer_profiles.types.tag_map


class UpdateDomainRequest(TypedDict, closed=True):
    domain_name: "capo_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    default_expiration_days: NotRequired[
        "capo_customer_profiles.types.expiration_days_integer.expirationDaysInteger"
    ]
    """<p>The default number of days until the data within the domain expires.</p>"""
    default_encryption_key: NotRequired[
        "capo_customer_profiles.types.encryption_key.encryptionKey"
    ]
    """<p>The default encryption key, which is an AWS managed key, is used when no specific type of encryption key is specified. It is used to encrypt all data before it is placed in permanent or semi-permanent storage. If specified as an empty string, it will clear any existing value.</p>"""
    dead_letter_queue_url: NotRequired[
        "capo_customer_profiles.types.sqs_queue_url.sqsQueueUrl"
    ]
    """<p>The URL of the SQS dead letter queue, which is used for reporting errors associated with ingesting data from third party applications. If specified as an empty string, it will clear any existing value. You must set up a policy on the DeadLetterQueue for the SendMessage operation to enable Amazon Connect Customer Profiles to send messages to the DeadLetterQueue.</p>"""
    matching: NotRequired[
        "capo_customer_profiles.types.matching_request.MatchingRequest"
    ]
    """<p>The process of matching duplicate profiles. If <code>Matching</code> = <code>true</code>, Amazon Connect Customer Profiles starts a weekly batch process called Identity Resolution Job. If you do not specify a date and time for Identity Resolution Job to run, by default it runs every Saturday at 12AM UTC to detect duplicate profiles in your domains. </p> <p>After the Identity Resolution Job completes, use the <a href="https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetMatches.html">GetMatches</a> API to return and review the results. Or, if you have configured <code>ExportingConfig</code> in the <code>MatchingRequest</code>, you can download the results from S3.</p>"""
    rule_based_matching: NotRequired[
        "capo_customer_profiles.types.rule_based_matching_request.RuleBasedMatchingRequest"
    ]
    """<p>The process of matching duplicate profiles using the rule-Based matching. If <code>RuleBasedMatching</code> = true, Connect Customer Customer Profiles will start to match and merge your profiles according to your configuration in the <code>RuleBasedMatchingRequest</code>. You can use the <code>ListRuleBasedMatches</code> and <code>GetSimilarProfiles</code> API to return and review the results. Also, if you have configured <code>ExportingConfig</code> in the <code>RuleBasedMatchingRequest</code>, you can download the results from S3.</p>"""
    data_store: NotRequired[
        "capo_customer_profiles.types.data_store_request.DataStoreRequest"
    ]
    """<p>Set to true to enabled data store for this domain.</p>"""
    tags: NotRequired["capo_customer_profiles.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDomainRequest) -> dict:
    out: dict = {}
    if "default_expiration_days" in value:
        out["DefaultExpirationDays"] = value["default_expiration_days"]
    if "default_encryption_key" in value:
        out["DefaultEncryptionKey"] = value["default_encryption_key"]
    if "dead_letter_queue_url" in value:
        out["DeadLetterQueueUrl"] = value["dead_letter_queue_url"]
    if "matching" in value:
        import capo_customer_profiles.types.matching_request

        out["Matching"] = capo_customer_profiles.types.matching_request.serialize_json(
            value["matching"]
        )
    if "rule_based_matching" in value:
        import capo_customer_profiles.types.rule_based_matching_request

        out["RuleBasedMatching"] = (
            capo_customer_profiles.types.rule_based_matching_request.serialize_json(
                value["rule_based_matching"]
            )
        )
    if "data_store" in value:
        import capo_customer_profiles.types.data_store_request

        out["DataStore"] = (
            capo_customer_profiles.types.data_store_request.serialize_json(
                value["data_store"]
            )
        )
    if "tags" in value:
        import capo_customer_profiles.types.tag_map

        out["Tags"] = capo_customer_profiles.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> UpdateDomainRequest:
    out: UpdateDomainRequest = {}  # type: ignore[typeddict-item]
    if data.get("DefaultExpirationDays") is not None:
        out["default_expiration_days"] = data["DefaultExpirationDays"]
    if data.get("DefaultEncryptionKey") is not None:
        out["default_encryption_key"] = data["DefaultEncryptionKey"]
    if data.get("DeadLetterQueueUrl") is not None:
        out["dead_letter_queue_url"] = data["DeadLetterQueueUrl"]
    if data.get("Matching") is not None:
        import capo_customer_profiles.types.matching_request

        out["matching"] = (
            capo_customer_profiles.types.matching_request.deserialize_json(
                data["Matching"]
            )
        )
    if data.get("RuleBasedMatching") is not None:
        import capo_customer_profiles.types.rule_based_matching_request

        out["rule_based_matching"] = (
            capo_customer_profiles.types.rule_based_matching_request.deserialize_json(
                data["RuleBasedMatching"]
            )
        )
    if data.get("DataStore") is not None:
        import capo_customer_profiles.types.data_store_request

        out["data_store"] = (
            capo_customer_profiles.types.data_store_request.deserialize_json(
                data["DataStore"]
            )
        )
    if data.get("Tags") is not None:
        import capo_customer_profiles.types.tag_map

        out["tags"] = capo_customer_profiles.types.tag_map.deserialize_json(
            data["Tags"]
        )
    return out
