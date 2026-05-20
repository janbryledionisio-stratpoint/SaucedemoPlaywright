import pytest
from utils.browser_manager import BrowserManager

@pytest.fixture(scope="session")
def browser_manager():
    manager = BrowserManager()
    manager.start_browser()
    yield manager
    manager.stop_browser()

@pytest.fixture(scope="function")
def page(browser_manager, request):
    # Create a new browser context and page
    context = browser_manager.new_context(
        record_video_dir="videos/",
        record_video_size={"width": 1280, "height": 720}
    )
    page = context.new_page()

    # Start tracing
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    yield page

    # Stop tracing and save per test
    test_name = request.node.name
    trace_path = f"traces/{test_name}.zip"  # make sure 'traces/' exists manually
    context.tracing.stop(path=trace_path)
    print(f"Trace saved at {trace_path}")

    # Close page and context
    page.close()
    context.close()