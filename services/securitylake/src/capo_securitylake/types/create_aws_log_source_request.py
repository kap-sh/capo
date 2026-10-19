"""Generated from Smithy shape ``com.amazonaws.securitylake#CreateAwsLogSourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_securitylake.types.aws_log_source_configuration_list


class CreateAwsLogSourceRequest(TypedDict, closed=True):
    sources: "capo_securitylake.types.aws_log_source_configuration_list.AwsLogSourceConfigurationList"
    """<p>Specify the natively-supported Amazon Web Services service to add as a source in Security Lake.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAwsLogSourceRequest) -> dict:
    out: dict = {}
    import capo_securitylake.types.aws_log_source_configuration_list

    out["sources"] = (
        capo_securitylake.types.aws_log_source_configuration_list.serialize_json(
            value["sources"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreateAwsLogSourceRequest:
    out: CreateAwsLogSourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("sources") is not None:
        import capo_securitylake.types.aws_log_source_configuration_list

        out["sources"] = (
            capo_securitylake.types.aws_log_source_configuration_list.deserialize_json(
                data["sources"]
            )
        )
    else:
        out["sources"] = []
    return out
