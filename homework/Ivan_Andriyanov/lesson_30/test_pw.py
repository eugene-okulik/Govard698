from playwright.sync_api import Page, Route, expect


def test_change_req(page: Page):
    def handle_route(route: Route):
        response = route.fetch()
        payload = response.json()

        payload["body"]["digitalMat"][0]["familyTypes"]["0"][
            "productName"
        ] = "яблокофон 17 про"

        route.fulfill(response=response, json=payload)

    page.route("**/shop/api/digital-mat**", handle_route)
    page.goto("https://www.apple.com/shop/buy-iphone")
    page.locator(".rf-hcard-img-wrapper").first.click()
    expect(page.get_by_role("heading", name="яблокофон 17 про")).to_be_visible()
