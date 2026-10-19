"""Generated from Smithy shape ``com.amazonaws.glue#Capabilities``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_glue.types.authentication_types
    import capo_glue.types.compute_environments
    import capo_glue.types.data_operations


class Capabilities(TypedDict, closed=True):
    supported_authentication_types: (
        "capo_glue.types.authentication_types.AuthenticationTypes"
    )
    """<p>A list of supported authentication types.</p>"""
    supported_data_operations: "capo_glue.types.data_operations.DataOperations"
    """<p>A list of supported data operations.</p>"""
    supported_compute_environments: (
        "capo_glue.types.compute_environments.ComputeEnvironments"
    )
    """<p>A list of supported compute environments.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Capabilities) -> dict:
    out: dict = {}
    import capo_glue.types.authentication_types

    out["SupportedAuthenticationTypes"] = (
        capo_glue.types.authentication_types.serialize_aws_json_1_1(
            value["supported_authentication_types"]
        )
    )
    import capo_glue.types.data_operations

    out["SupportedDataOperations"] = (
        capo_glue.types.data_operations.serialize_aws_json_1_1(
            value["supported_data_operations"]
        )
    )
    import capo_glue.types.compute_environments

    out["SupportedComputeEnvironments"] = (
        capo_glue.types.compute_environments.serialize_aws_json_1_1(
            value["supported_compute_environments"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> Capabilities:
    out: Capabilities = {}  # type: ignore[typeddict-item]
    if data.get("SupportedAuthenticationTypes") is not None:
        import capo_glue.types.authentication_types

        out["supported_authentication_types"] = (
            capo_glue.types.authentication_types.deserialize_aws_json_1_1(
                data["SupportedAuthenticationTypes"]
            )
        )
    else:
        out["supported_authentication_types"] = []
    if data.get("SupportedDataOperations") is not None:
        import capo_glue.types.data_operations

        out["supported_data_operations"] = (
            capo_glue.types.data_operations.deserialize_aws_json_1_1(
                data["SupportedDataOperations"]
            )
        )
    else:
        out["supported_data_operations"] = []
    if data.get("SupportedComputeEnvironments") is not None:
        import capo_glue.types.compute_environments

        out["supported_compute_environments"] = (
            capo_glue.types.compute_environments.deserialize_aws_json_1_1(
                data["SupportedComputeEnvironments"]
            )
        )
    else:
        out["supported_compute_environments"] = []
    return out
