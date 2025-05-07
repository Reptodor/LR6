using UnityEngine;

public class Mover
{
    private readonly Player _player;
    private readonly Rigidbody _rigidbody;
    private readonly InputSystem _inputSystem;
    private readonly Stamina _stamina;
    private readonly float _baseSpeed;
    private readonly float _sprintMultiplier;

    private bool _isSprinting;
    
    public Mover(Player player, Rigidbody rigidbody, InputSystem inputSystem, Stamina stamina, float speed, float sprintMultiplier)
    {
        _player = player;
        _rigidbody = rigidbody;
        _inputSystem = inputSystem;
        _stamina = stamina;
        _baseSpeed = speed;
        _sprintMultiplier = sprintMultiplier;
    }

    public void SetSprint(bool isSprinting)
    {
        _isSprinting = isSprinting;
    }

    public void Move()
    {
        float speed = _baseSpeed;

        if (_isSprinting && _stamina.CanUse)
        {
            _stamina.Use();
            speed *= _sprintMultiplier;

        }
        else
        {
            _stamina.Restore();
        }

        Vector3 direcrion = _player.transform.right * _inputSystem.GetMovementAxis().x +
                            _player.transform.forward * _inputSystem.GetMovementAxis().z;

        _rigidbody.velocity = new Vector3(direcrion.x * speed, _rigidbody.velocity.y, direcrion.z * speed);
    }
}
