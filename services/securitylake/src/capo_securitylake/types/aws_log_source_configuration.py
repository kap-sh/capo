"""Generated from Smithy shape ``com.amazonaws.securitylake#AwsLogSourceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securitylake.types.account_list
    import capo_securitylake.types.aws_log_source_name
    import capo_securitylake.types.aws_log_source_version
    import capo_securitylake.types.region_list


class AwsLogSourceConfiguration(TypedDict, closed=True):
    accounts: NotRequired["capo_securitylake.types.account_list.AccountList"]
    """<p>Specify the Amazon Web Services account information where you want to enable Security Lake.</p>"""
    regions: "capo_securitylake.types.region_list.RegionList"
    """<p>Specify the Regions where you want to enable Security Lake.</p>"""
    source_name: "capo_securitylake.types.aws_log_source_name.AwsLogSourceName"
    """<p>The name for a Amazon Web Services source. </p>"""
    source_version: "capo_securitylake.types.aws_log_source_version.AwsLogSourceVersion"
    """<p>The version for a Amazon Web Services source. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsLogSourceConfiguration) -> dict:
    out: dict = {}
    if "accounts" in value:
        import capo_securitylake.types.account_list

        out["accounts"] = capo_securitylake.types.account_list.serialize_json(
            value["accounts"]
        )
    import capo_securitylake.types.region_list

    out["regions"] = capo_securitylake.types.region_list.serialize_json(
        value["regions"]
    )
    import capo_securitylake.types.aws_log_source_name

    out["sourceName"] = capo_securitylake.types.aws_log_source_name.serialize_json(
        value["source_name"]
    )
    out["sourceVersion"] = value.get("source_version", "latest")
    return out


def deserialize_json(data: dict) -> AwsLogSourceConfiguration:
    out: AwsLogSourceConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("accounts") is not None:
        import capo_securitylake.types.account_list

        out["accounts"] = capo_securitylake.types.account_list.deserialize_json(
            data["accounts"]
        )
    if data.get("regions") is not None:
        import capo_securitylake.types.region_list

        out["regions"] = capo_securitylake.types.region_list.deserialize_json(
            data["regions"]
        )
    else:
        out["regions"] = []
    if data.get("sourceName") is not None:
        import capo_securitylake.types.aws_log_source_name

        out["source_name"] = (
            capo_securitylake.types.aws_log_source_name.deserialize_json(
                data["sourceName"]
            )
        )
    else:
        import typing

        out["source_name"] = typing.cast(
            "capo_securitylake.types.aws_log_source_name.AwsLogSourceName", ""
        )
    if data.get("sourceVersion") is not None:
        out["source_version"] = data["sourceVersion"]
    else:
        out["source_version"] = "latest"
    return out
