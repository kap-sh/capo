"""Generated from Smithy shape ``com.amazonaws.securitylake#DataLakeAutoEnableNewAccountConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_securitylake.types.aws_log_source_resource_list
    import capo_securitylake.types.region


class DataLakeAutoEnableNewAccountConfiguration(TypedDict, closed=True):
    region: "capo_securitylake.types.region.Region"
    """<p>The Amazon Web Services Regions where Security Lake is automatically enabled.</p>"""
    sources: (
        "capo_securitylake.types.aws_log_source_resource_list.AwsLogSourceResourceList"
    )
    """<p>The Amazon Web Services sources that are automatically enabled in Security Lake.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataLakeAutoEnableNewAccountConfiguration) -> dict:
    out: dict = {}
    out["region"] = value["region"]
    import capo_securitylake.types.aws_log_source_resource_list

    out["sources"] = (
        capo_securitylake.types.aws_log_source_resource_list.serialize_json(
            value["sources"]
        )
    )
    return out


def deserialize_json(data: dict) -> DataLakeAutoEnableNewAccountConfiguration:
    out: DataLakeAutoEnableNewAccountConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("region") is not None:
        out["region"] = data["region"]
    else:
        out["region"] = ""
    if data.get("sources") is not None:
        import capo_securitylake.types.aws_log_source_resource_list

        out["sources"] = (
            capo_securitylake.types.aws_log_source_resource_list.deserialize_json(
                data["sources"]
            )
        )
    else:
        out["sources"] = []
    return out
