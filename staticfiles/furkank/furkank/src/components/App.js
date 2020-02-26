import React from "react";

import { CssBaseline } from "@material-ui/core";
import { createMuiTheme, ThemeProvider } from "@material-ui/core/styles";
import Mainpage from "./Mainpage";

const theme = createMuiTheme({
  palette: {
    primary: {
      main: "#ffc107"
    },
    secondary: {
      main: "#9575cd"
    }
  }
});

function App() {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Mainpage />
    </ThemeProvider>
  );
}

export default App;
