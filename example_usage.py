"""Example usage for Dynamic Landing Page Personalizer."""
from client import LandingPagePersonalizer

if __name__ == "__main__":
    view = LandingPagePersonalizer.personalize_view({
        "utm_source": "linkedin.com",
        "detected_role": "VP of Engineering"
    })
    print("Matched ICP Segment:", view["matched_segment"])
    print("Headline:", view["hero_headline"])
    print("CTA:", view["primary_cta"])
