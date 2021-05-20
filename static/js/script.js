let password = prompt('Input vendor\'s password', '');
let codes = ['1BeA1F', 'E1fF1d', '56e585', '35A4ED', 'Ebac43', 'B81C6D', '889D4D', '3aAf2c', 'a734b4', 'C3ec04', 'ffAb47', '15Fe98', 'e09F3b', 'eEf23F', '2F2ecE', 'C9D789', 'ad4bad', 'Bd141C', 'ac055c', '5c7Fd4']
while (!codes.includes(password)){
    password = prompt('Incorrect, please try again')
}