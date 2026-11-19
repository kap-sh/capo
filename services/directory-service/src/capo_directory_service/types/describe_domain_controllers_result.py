"""Generated from Smithy shape ``com.amazonaws.directoryservice#DescribeDomainControllersResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.domain_controllers
    import capo_directory_service.types.next_token


class DescribeDomainControllersResult(TypedDict, closed=True):
    domain_controllers: NotRequired[
        "capo_directory_service.types.domain_controllers.DomainControllers"
    ]
    """<p>List of the <a>DomainController</a> objects that were retrieved.</p>"""
    next_token: NotRequired["capo_directory_service.types.next_token.NextToken"]
    """<p>If not null, more results are available. Pass this value for the <code>NextToken</code> parameter in a subsequent call to <a>DescribeDomainControllers</a> retrieve the next set of items.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDomainControllersResult) -> dict:
    out: dict = {}
    if "domain_controllers" in value:
        import capo_directory_service.types.domain_controllers

        out["DomainControllers"] = (
            capo_directory_service.types.domain_controllers.serialize_aws_json_1_1(
                value["domain_controllers"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDomainControllersResult:
    out: DescribeDomainControllersResult = {}  # type: ignore[typeddict-item]
    if data.get("DomainControllers") is not None:
        import capo_directory_service.types.domain_controllers

        out["domain_controllers"] = (
            capo_directory_service.types.domain_controllers.deserialize_aws_json_1_1(
                data["DomainControllers"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeDomainControllersResult) -> dict:
    out: dict = {}
    if "domain_controllers" in value:
        import capo_directory_service.types.domain_controllers

        out["DomainControllers"] = (
            capo_directory_service.types.domain_controllers.serialize_cbor(
                value["domain_controllers"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> DescribeDomainControllersResult:
    out: DescribeDomainControllersResult = {}  # type: ignore[typeddict-item]
    if data.get("DomainControllers") is not None:
        import capo_directory_service.types.domain_controllers

        out["domain_controllers"] = (
            capo_directory_service.types.domain_controllers.deserialize_cbor(
                data["DomainControllers"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
