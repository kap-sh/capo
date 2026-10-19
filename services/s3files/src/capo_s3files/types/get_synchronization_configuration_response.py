"""Generated from Smithy shape ``com.amazonaws.s3files#GetSynchronizationConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_s3files.types.expiration_data_rule_list
    import capo_s3files.types.import_data_rule_list


class GetSynchronizationConfigurationResponse(TypedDict, closed=True):
    latest_version_number: NotRequired["int"]
    """<p>The version number of the synchronization configuration. Use this value with <code>PutSynchronizationConfiguration</code> to ensure optimistic concurrency control.</p>"""
    import_data_rules: "capo_s3files.types.import_data_rule_list.ImportDataRuleList"
    """<p>An array of import data rules that control how data is imported from S3 into the file system.</p>"""
    expiration_data_rules: (
        "capo_s3files.types.expiration_data_rule_list.ExpirationDataRuleList"
    )
    """<p>An array of expiration data rules that control when cached data expires from the file system.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSynchronizationConfigurationResponse) -> dict:
    out: dict = {}
    if "latest_version_number" in value:
        out["latestVersionNumber"] = value["latest_version_number"]
    import capo_s3files.types.import_data_rule_list

    out["importDataRules"] = capo_s3files.types.import_data_rule_list.serialize_json(
        value["import_data_rules"]
    )
    import capo_s3files.types.expiration_data_rule_list

    out["expirationDataRules"] = (
        capo_s3files.types.expiration_data_rule_list.serialize_json(
            value["expiration_data_rules"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetSynchronizationConfigurationResponse:
    out: GetSynchronizationConfigurationResponse = {}  # type: ignore[typeddict-item]
    if data.get("latestVersionNumber") is not None:
        out["latest_version_number"] = data["latestVersionNumber"]
    if data.get("importDataRules") is not None:
        import capo_s3files.types.import_data_rule_list

        out["import_data_rules"] = (
            capo_s3files.types.import_data_rule_list.deserialize_json(
                data["importDataRules"]
            )
        )
    else:
        out["import_data_rules"] = []
    if data.get("expirationDataRules") is not None:
        import capo_s3files.types.expiration_data_rule_list

        out["expiration_data_rules"] = (
            capo_s3files.types.expiration_data_rule_list.deserialize_json(
                data["expirationDataRules"]
            )
        )
    else:
        out["expiration_data_rules"] = []
    return out
