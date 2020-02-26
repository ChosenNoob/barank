import React from "react";

import useMediaQuery from "@material-ui/core/useMediaQuery";
import Cookie from "./Cookie.svg";

import { makeStyles, useTheme } from "@material-ui/core/styles";
import { Container } from "@material-ui/core";
import Grid from "@material-ui/core/Grid";
import Paper from "@material-ui/core/Paper";
import TextField from "@material-ui/core/TextField";
import Link from "@material-ui/core/Link";
import Typography from "@material-ui/core/Typography";
import Button from "@material-ui/core/Button";

const useStyles = makeStyles(theme => ({
  paper: {
    padding: theme.spacing(3)
  }
}));

export default function Mainpage() {
  const theme = useTheme();
  const classes = useStyles();

  return (
    <Container
      maxWidth={useMediaQuery(theme.breakpoints.up("md")) ? "md" : "xl"}
      style={{
        marginTop: useMediaQuery(theme.breakpoints.up("md"))
          ? theme.spacing(25)
          : 0
      }}
    >
      <Grid
        container
        justify="center"
        alignItems="center"
        direction={useMediaQuery(theme.breakpoints.up("md")) ? "row" : "column"}
      >
        <Grid item>
          <img src={Cookie} alt="logo" />
        </Grid>
        <Grid item>
          <Paper className={classes.paper}>
            <Grid
              container
              direction="column"
              justify="center"
              alignItems="center"
              spacing={3}
            >
              <Grid item>
                <Typography component="h1" variant="h5">
                  Sign in
                </Typography>
              </Grid>
              <Grid item>
                <TextField
                  variant="outlined"
                  margin="normal"
                  required
                  id="email"
                  label="Username"
                  name="email"
                  autoFocus
                />
              </Grid>
              <Grid item>
                <TextField
                  variant="outlined"
                  margin="normal"
                  required
                  name="password"
                  label="Password"
                  type="password"
                  id="password"
                />
              </Grid>
              <Grid item>
                <Button type="submit" variant="contained" color="primary">
                  Sign In
                </Button>
              </Grid>
              <Grid item>
                <Grid
                  container
                  justify="center"
                  alignItems="center"
                  spacing={5}
                >
                  <Grid item>
                    <Link href="#" variant="body2">
                      {"Forgot password?"}
                    </Link>
                  </Grid>
                  <Grid item>
                    <Link href="#" variant="body2">
                      {"Sign Up"}
                    </Link>
                  </Grid>
                </Grid>
              </Grid>
            </Grid>
          </Paper>
        </Grid>
      </Grid>
    </Container>
  );
}
