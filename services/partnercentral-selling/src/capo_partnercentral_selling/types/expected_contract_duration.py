"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ExpectedContractDuration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.expected_contract_duration_term


class ExpectedContractDuration(TypedDict, closed=True):
    term: "capo_partnercentral_selling.types.expected_contract_duration_term.ExpectedContractDurationTerm"
    """<p>The unit of measurement for the contract duration value. Currently accepts only <code>Months</code>.</p>"""
    value: "str"
    """<p>A String representation of the contract duration as an integer, expressed in the unit defined by <code>Term</code>. Valid values range from <code>1</code> to <code>144</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExpectedContractDuration) -> dict:
    out: dict = {}
    import capo_partnercentral_selling.types.expected_contract_duration_term

    out["Term"] = (
        capo_partnercentral_selling.types.expected_contract_duration_term.serialize_aws_json_1_0(
            value["term"]
        )
    )
    out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ExpectedContractDuration:
    out: ExpectedContractDuration = {}  # type: ignore[typeddict-item]
    if data.get("Term") is not None:
        import capo_partnercentral_selling.types.expected_contract_duration_term

        out["term"] = (
            capo_partnercentral_selling.types.expected_contract_duration_term.deserialize_aws_json_1_0(
                data["Term"]
            )
        )
    else:
        import typing

        out["term"] = typing.cast(
            "capo_partnercentral_selling.types.expected_contract_duration_term.ExpectedContractDurationTerm",
            "",
        )
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        out["value"] = ""
    return out
