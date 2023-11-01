import styled from 'styled-components/native';

const SplashIcon = styled.Image`
  color: white;
  font-family: 'Cookie-Regular';
  font-size: 100px;
  margin: auto;
  overflow: visible;
  text-shadow: 1px 1px 1px rgba(0, 0, 0, 0.75);
`;

SplashIcon.defaultProps = {
  source: require('../../assets/images/chefHat.png'),
};

export default SplashIcon;
