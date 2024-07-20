# Enviroment independant scss compilation

## Trigger one-time compilaion

    sass [your scss file location] [where your css file needs to be stored]

## Trigger continous compilation for files

    sass --watch static/scss/index.scss static/css/index.css

## Trigger continous compilation for directories

    sass --watch static/scss/:static/css/

## CSS debuging

- {
  outline: 1px red dashed;
  }

```
* {
  outline: 1px red dashed;
}

```
