"""Generated from Smithy shape ``com.amazonaws.inspector#DescribeRulesPackagesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector.types.failed_items
    import capo_inspector.types.rules_package_list


class DescribeRulesPackagesResponse(TypedDict, closed=True):
    rules_packages: "capo_inspector.types.rules_package_list.RulesPackageList"
    """<p>Information about the rules package.</p>"""
    failed_items: "capo_inspector.types.failed_items.FailedItems"
    """<p>Rules package details that cannot be described. An error code is provided for each failed item.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeRulesPackagesResponse) -> dict:
    out: dict = {}
    import capo_inspector.types.rules_package_list

    out["rulesPackages"] = (
        capo_inspector.types.rules_package_list.serialize_aws_json_1_1(
            value["rules_packages"]
        )
    )
    import capo_inspector.types.failed_items

    out["failedItems"] = capo_inspector.types.failed_items.serialize_aws_json_1_1(
        value["failed_items"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeRulesPackagesResponse:
    out: DescribeRulesPackagesResponse = {}  # type: ignore[typeddict-item]
    if data.get("rulesPackages") is not None:
        import capo_inspector.types.rules_package_list

        out["rules_packages"] = (
            capo_inspector.types.rules_package_list.deserialize_aws_json_1_1(
                data["rulesPackages"]
            )
        )
    else:
        out["rules_packages"] = []
    if data.get("failedItems") is not None:
        import capo_inspector.types.failed_items

        out["failed_items"] = (
            capo_inspector.types.failed_items.deserialize_aws_json_1_1(
                data["failedItems"]
            )
        )
    else:
        out["failed_items"] = {}
    return out
