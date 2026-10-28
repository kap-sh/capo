"""Generated from Smithy shape ``com.amazonaws.acm#CertificateFilterStatement``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_acm.errors import DeserializationError, SerializationError
from capo_acm.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_acm.types.certificate_filter
    import capo_acm.types.certificate_filter_statement
    import capo_acm.types.certificate_filter_statement_list


class CertificateFilterStatementAndMember(TypedDict, closed=True):
    And: "capo_acm.types.certificate_filter_statement_list.CertificateFilterStatementList"


class CertificateFilterStatementOrMember(TypedDict, closed=True):
    Or: "capo_acm.types.certificate_filter_statement_list.CertificateFilterStatementList"


class CertificateFilterStatementNotMember(TypedDict, closed=True):
    Not: "capo_acm.types.certificate_filter_statement.CertificateFilterStatement"


class CertificateFilterStatementFilterMember(TypedDict, closed=True):
    Filter: "capo_acm.types.certificate_filter.CertificateFilter"


CertificateFilterStatement: TypeAlias = (
    CertificateFilterStatementAndMember
    | CertificateFilterStatementOrMember
    | CertificateFilterStatementNotMember
    | CertificateFilterStatementFilterMember
    | UnknownUnionMember
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CertificateFilterStatement) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"CertificateFilterStatement: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "And" in value:
        import capo_acm.types.certificate_filter_statement_list

        return {
            "And": capo_acm.types.certificate_filter_statement_list.serialize_aws_json_1_1(
                value["And"]
            )
        }
    elif "Or" in value:
        import capo_acm.types.certificate_filter_statement_list

        return {
            "Or": capo_acm.types.certificate_filter_statement_list.serialize_aws_json_1_1(
                value["Or"]
            )
        }
    elif "Not" in value:
        import capo_acm.types.certificate_filter_statement

        return {
            "Not": capo_acm.types.certificate_filter_statement.serialize_aws_json_1_1(
                value["Not"]
            )
        }
    elif "Filter" in value:
        import capo_acm.types.certificate_filter

        return {
            "Filter": capo_acm.types.certificate_filter.serialize_aws_json_1_1(
                value["Filter"]
            )
        }
    else:
        raise SerializationError("CertificateFilterStatement: no variant present")


def deserialize_aws_json_1_1(data: dict) -> CertificateFilterStatement:
    if data.get("And") is not None:
        import capo_acm.types.certificate_filter_statement_list

        return {
            "And": capo_acm.types.certificate_filter_statement_list.deserialize_aws_json_1_1(
                data["And"]
            )
        }
    elif data.get("Or") is not None:
        import capo_acm.types.certificate_filter_statement_list

        return {
            "Or": capo_acm.types.certificate_filter_statement_list.deserialize_aws_json_1_1(
                data["Or"]
            )
        }
    elif data.get("Not") is not None:
        import capo_acm.types.certificate_filter_statement

        return {
            "Not": capo_acm.types.certificate_filter_statement.deserialize_aws_json_1_1(
                data["Not"]
            )
        }
    elif data.get("Filter") is not None:
        import capo_acm.types.certificate_filter

        return {
            "Filter": capo_acm.types.certificate_filter.deserialize_aws_json_1_1(
                data["Filter"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "CertificateFilterStatement: no recognized variant key"
        )
