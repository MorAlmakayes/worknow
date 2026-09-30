import { render, screen } from "@testing-library/react";

import RootLayout from "@/app/layout";
import HomePage from "@/app/page";

describe("HomePage", () => {
  it("renders the Hebrew placeholder heading", () => {
    render(<HomePage />);

    expect(
      screen.getByRole("heading", { level: 1, name: "ברוכים הבאים ל-WorkNow" }),
    ).toBeInTheDocument();
  });
});

describe("RootLayout", () => {
  it("sets Hebrew language and right-to-left direction", () => {
    const html = RootLayout({ children: null });

    expect(html.props.lang).toBe("he");
    expect(html.props.dir).toBe("rtl");
  });
});
