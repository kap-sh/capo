"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#LicenseRecommendationOption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.license_edition
    import capo_compute_optimizer.types.license_model
    import capo_compute_optimizer.types.operating_system
    import capo_compute_optimizer.types.rank
    import capo_compute_optimizer.types.savings_opportunity


class LicenseRecommendationOption(TypedDict, closed=True):
    rank: "capo_compute_optimizer.types.rank.Rank"
    """<p> The rank of the license recommendation option. </p> <p> The top recommendation option is ranked as <code>1</code>. </p>"""
    operating_system: NotRequired[
        "capo_compute_optimizer.types.operating_system.OperatingSystem"
    ]
    """<p> The operating system of a license recommendation option. </p>"""
    license_edition: NotRequired[
        "capo_compute_optimizer.types.license_edition.LicenseEdition"
    ]
    """<p> The recommended edition of the license for the application that runs on the instance. </p>"""
    license_model: NotRequired[
        "capo_compute_optimizer.types.license_model.LicenseModel"
    ]
    """<p> The recommended license type associated with the instance. </p>"""
    savings_opportunity: NotRequired[
        "capo_compute_optimizer.types.savings_opportunity.SavingsOpportunity"
    ]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LicenseRecommendationOption) -> dict:
    out: dict = {}
    out["rank"] = value.get("rank", 0)
    if "operating_system" in value:
        out["operatingSystem"] = value["operating_system"]
    if "license_edition" in value:
        import capo_compute_optimizer.types.license_edition

        out["licenseEdition"] = (
            capo_compute_optimizer.types.license_edition.serialize_aws_json_1_0(
                value["license_edition"]
            )
        )
    if "license_model" in value:
        import capo_compute_optimizer.types.license_model

        out["licenseModel"] = (
            capo_compute_optimizer.types.license_model.serialize_aws_json_1_0(
                value["license_model"]
            )
        )
    if "savings_opportunity" in value:
        import capo_compute_optimizer.types.savings_opportunity

        out["savingsOpportunity"] = (
            capo_compute_optimizer.types.savings_opportunity.serialize_aws_json_1_0(
                value["savings_opportunity"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> LicenseRecommendationOption:
    out: LicenseRecommendationOption = {}  # type: ignore[typeddict-item]
    if data.get("rank") is not None:
        out["rank"] = data["rank"]
    else:
        out["rank"] = 0
    if data.get("operatingSystem") is not None:
        out["operating_system"] = data["operatingSystem"]
    if data.get("licenseEdition") is not None:
        import capo_compute_optimizer.types.license_edition

        out["license_edition"] = (
            capo_compute_optimizer.types.license_edition.deserialize_aws_json_1_0(
                data["licenseEdition"]
            )
        )
    if data.get("licenseModel") is not None:
        import capo_compute_optimizer.types.license_model

        out["license_model"] = (
            capo_compute_optimizer.types.license_model.deserialize_aws_json_1_0(
                data["licenseModel"]
            )
        )
    if data.get("savingsOpportunity") is not None:
        import capo_compute_optimizer.types.savings_opportunity

        out["savings_opportunity"] = (
            capo_compute_optimizer.types.savings_opportunity.deserialize_aws_json_1_0(
                data["savingsOpportunity"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LicenseRecommendationOption) -> dict:
    out: dict = {}
    out["rank"] = value.get("rank", 0)
    if "operating_system" in value:
        out["operatingSystem"] = value["operating_system"]
    if "license_edition" in value:
        import capo_compute_optimizer.types.license_edition

        out["licenseEdition"] = (
            capo_compute_optimizer.types.license_edition.serialize_cbor(
                value["license_edition"]
            )
        )
    if "license_model" in value:
        import capo_compute_optimizer.types.license_model

        out["licenseModel"] = capo_compute_optimizer.types.license_model.serialize_cbor(
            value["license_model"]
        )
    if "savings_opportunity" in value:
        import capo_compute_optimizer.types.savings_opportunity

        out["savingsOpportunity"] = (
            capo_compute_optimizer.types.savings_opportunity.serialize_cbor(
                value["savings_opportunity"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> LicenseRecommendationOption:
    out: LicenseRecommendationOption = {}  # type: ignore[typeddict-item]
    if data.get("rank") is not None:
        out["rank"] = data["rank"]
    else:
        out["rank"] = 0
    if data.get("operatingSystem") is not None:
        out["operating_system"] = data["operatingSystem"]
    if data.get("licenseEdition") is not None:
        import capo_compute_optimizer.types.license_edition

        out["license_edition"] = (
            capo_compute_optimizer.types.license_edition.deserialize_cbor(
                data["licenseEdition"]
            )
        )
    if data.get("licenseModel") is not None:
        import capo_compute_optimizer.types.license_model

        out["license_model"] = (
            capo_compute_optimizer.types.license_model.deserialize_cbor(
                data["licenseModel"]
            )
        )
    if data.get("savingsOpportunity") is not None:
        import capo_compute_optimizer.types.savings_opportunity

        out["savings_opportunity"] = (
            capo_compute_optimizer.types.savings_opportunity.deserialize_cbor(
                data["savingsOpportunity"]
            )
        )
    return out
