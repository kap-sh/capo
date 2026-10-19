"""Generated from Smithy shape ``com.amazonaws.cloudsearch#UpdateScalingParametersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudsearch._protocol.xml import Element
from capo_cloudsearch.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudsearch.types.domain_name
    import capo_cloudsearch.types.scaling_parameters


class UpdateScalingParametersRequest(TypedDict, closed=True):
    domain_name: "capo_cloudsearch.types.domain_name.DomainName"
    scaling_parameters: "capo_cloudsearch.types.scaling_parameters.ScalingParameters"


# --- awsQuery ser/de ---
def serialize_query(
    value: UpdateScalingParametersRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}DomainName", str(value["domain_name"])))
    import capo_cloudsearch.types.scaling_parameters

    capo_cloudsearch.types.scaling_parameters.serialize_query(
        value["scaling_parameters"], pairs, f"{key_prefix}ScalingParameters"
    )


def deserialize_query(el: Element) -> UpdateScalingParametersRequest:
    out: UpdateScalingParametersRequest = {}  # type: ignore[typeddict-item]
    child_domain_name = el.find("DomainName")
    if child_domain_name is not None:
        out["domain_name"] = str(child_domain_name.text or "")
    else:
        out["domain_name"] = ""
    child_scaling_parameters = el.find("ScalingParameters")
    if child_scaling_parameters is not None:
        import capo_cloudsearch.types.scaling_parameters

        out["scaling_parameters"] = (
            capo_cloudsearch.types.scaling_parameters.deserialize_query(
                child_scaling_parameters
            )
        )
    else:
        raise DeserializationError(
            "UpdateScalingParametersRequest.scaling_parameters required"
        )
    return out
