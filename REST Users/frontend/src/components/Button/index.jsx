import PropTypes from "prop-types";

const Button = ({ conteudo }) => {
  return <button><a href="">{conteudo}</a></button>;
};

// Definição dos tipos das props
Button.propTypes = {
  conteudo: PropTypes.string.isRequired, // Define 'conteudo' como obrigatório e do tipo string
};

export default Button;